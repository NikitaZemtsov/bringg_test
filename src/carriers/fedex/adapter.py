from src.schemas.track import Checkpoint, ErrorCode, Locale, TrackErrorResponse, TrackingStage, TrackSuccessfulResponse

from .schemas import Code, DeliveryCode, Events, Severity, TrackReply


class ResponseBuilder:
    def build_track_response(
        self, carrier, tracking_number, track_reply: TrackReply
    ) -> TrackSuccessfulResponse | TrackErrorResponse | None:
        track_details = track_reply.completed_track_details.track_details
        if track_details.notification.severity == Severity.SUCCESS:
            response = TrackSuccessfulResponse(carrier=carrier, tracking_number=tracking_number)
            response.locale = self.__locale(track_reply)
            response.status = track_details.status_detail.description
            if track_details.status_detail.code == DeliveryCode.DELIVERED:
                response.delivered = True
                response.delivery_date = self.__checkpoint(track_details.events[0]).time
            response.checkpoints = [self.__checkpoint(event) for event in track_details.events]
            response.tracking_stage = self.__tracking_stage(track_details.status_detail.code)
            return response
        if track_details.notification.severity == Severity.ERROR:
            code = self.__error_code(track_details.notification.code)
            message = track_details.notification.localized_message
            return TrackErrorResponse(code=code, message=message)
        return None

    @staticmethod
    def __locale(track_reply: TrackReply):
        code = track_reply.transaction_detail.localization.locale_code.upper()
        language = track_reply.transaction_detail.localization.language_code.upper()
        return getattr(Locale, f'{language}_{code}')

    def __error_code(self, code):
        if code == Code.NOT_FOUND:
            return ErrorCode.CARRIER_NO_SHIPMENT_FOUND
        return ErrorCode.CARRIER_EXCEPTION

    @staticmethod
    def __tracking_stage(stage_code):
        stage = None
        match stage_code:
            case DeliveryCode.DELIVERED:
                stage = TrackingStage.DELIVERED
            case DeliveryCode.ON__FED_EX_VEHICLE_FOR_DELIVERY:
                stage = TrackingStage.IN_TRANSIT
            case DeliveryCode.AT_LOCAL_FEDEX_FACILITY:
                stage = TrackingStage.CHECKED_IN
            case DeliveryCode.ON_THE_WAY:
                stage = TrackingStage.OUT_FOR_DELIVERY
            case DeliveryCode.DEPARTED_FEDEX_LOCATION:
                stage = TrackingStage.IN_TRANSIT
            case DeliveryCode.PICKED_UP:
                stage = TrackingStage.PICKED_UP
        return stage

    def __checkpoint(self, event: Events):
        description = event.event_description
        status = description
        tracking_stage = self.__tracking_stage(event.event_type)
        time = event.timestamp
        return Checkpoint(description=description, status=status, tracking_stage=tracking_stage, time=time)
