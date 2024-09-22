from src.schemas.track import Checkpoint, Locale, TrackingStage, TrackSuccessfulResponse

from .schemas import DeliveryCode, Events, Severity, TrackReply


class ResponseBuilder:
    def build_track_response(self, carrier, tracking_number, track_reply: TrackReply) -> TrackSuccessfulResponse:
        if TrackReply.completed_track_details.track_details.notification.severity == Severity.SUCCESS:
            track_details = track_reply.completed_track_details.track_details
            response = TrackSuccessfulResponse(carrier=carrier, tracking_number=tracking_number)
            response.locale = self.__locale(track_reply)
            response.status = track_details.status_detail.description
            if track_details.status_detail.code == DeliveryCode.DELIVERED:
                response.delivered = True
                response.delivery_date = self.__checkpoint(track_details.events[0]).time
            response.checkpoints = [self.__checkpoint(event) for event in track_details.events]

    def __locale(self, track_reply: TrackReply):
        code = track_reply.transaction_detail.localization.locale_code.upper()
        language = track_reply.transaction_detail.localization.language_code.lower()
        return getattr(Locale, f'{language}_{code}')

    def __tracking_stage(self, stage_code):
        stage = None
        match stage_code:
            case DeliveryCode.DELIVERED:
                stage = TrackingStage.DELIVERED
        return stage

    def __checkpoint(self, event: Events):
        description = event.event_description
        status = description
        tracking_stage = self.__tracking_stage(event.event_type)
        time = event.timestamp
        return Checkpoint(description=description, status=status, tracking_stage=tracking_stage, time=time)
