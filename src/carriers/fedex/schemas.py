import re

from pydantic_xml import BaseXmlModel, attr, element

from .models import FedExCredentialsModel


class ParentCredential(BaseXmlModel):
    key: str = element(tag='Key')
    password: str = element(tag='Password')


class UserCredential(BaseXmlModel):
    key: str = element(tag='Key')
    password: str = element(tag='Password')


class WebAuthenticationDetail(BaseXmlModel):
    parent_credential: ParentCredential = element(tag='ParentCredential')
    user_credential: UserCredential = element(tag='UserCredential')

    @staticmethod
    def convert_to_xml_model(credential: FedExCredentialsModel):
        return WebAuthenticationDetail(
            parent_credential=ParentCredential(key=credential.parent_key, password=credential.parent_password),
            user_credential=UserCredential(key=credential.user_key, password=credential.user_password),
        )


class ClientDetail(BaseXmlModel):
    account_number: str = element(tag='AccountNumber')
    meter_number: str = element(tag='MeterNumber')

    @staticmethod
    def convert_to_xml_model(credential: FedExCredentialsModel):
        return ClientDetail(account_number=credential.account_number, meter_number=credential.meter_number)


class Localization(BaseXmlModel):
    language_code: str = element(default='EN', tag='LanguageCode')
    locale_code: str = element(default='US', tag='LocaleCode')


class TransactionDetail(BaseXmlModel):
    customer_transaction_id: str = element(default='Track By Number_v14', tag='CustomerTransactionId')
    localization: Localization = element(default_factory=Localization, tag='Localization')


class Version(BaseXmlModel):
    service_id: str = element(default='trck', tag='ServiceId')
    major: int = element(default=14, tag='Major')
    intermediate: int = element(default=0, tag='Intermediate')
    minor: int = element(default=0, tag='Minor')


class PackageIdentifier(BaseXmlModel):
    type: str = element(default='TRACKING_NUMBER_OR_DOORTAG', tag='Type')
    value: str = element(tag='Value', default='')


class SelectionDetails(BaseXmlModel):
    carrier_code: str = element(default='FDXE', tag='CarrierCode')
    package_identifier: PackageIdentifier = element(tag='PackageIdentifier', default_factory=PackageIdentifier)
    shipment_account_number: str = element(tag='ShipmentAccountNumber', default='')
    secure_spod_account: str = element(tag='SecureSpodAccount', default='')
    destination: str = element(tag='Destination', default='')
    geographic_coordinates: str = element(tag='GeographicCoordinates', default='')


class TrackRequest(BaseXmlModel, tag='TrackRequest'):
    xmlns_xsi: str = attr(name='xmlns:xsi', default='http://www.w3.org/2001/XMLSchema-instance')
    xmlns_xsd: str = attr(name='xmlns:xsd', default='http://www.w3.org/2001/XMLSchema')
    xmlns: str = attr(name='xmlns', default='http://fedex.com/ws/track/v14')
    web_authentication_detail: WebAuthenticationDetail = element(tag='WebAuthenticationDetail')
    client_detail: ClientDetail = element(tag='ClientDetail')
    transaction_detail: TransactionDetail = element(tag='TransactionDetail', default_factory=TransactionDetail)
    version: Version = element(tag='Version', default_factory=Version)
    selection_details: SelectionDetails = element(tag='SelectionDetails', default_factory=SelectionDetails)


class Notifications(BaseXmlModel):
    severity: str = element(tag='Severity')
    source: str = element(tag='Source')
    code: int = element(tag='Code')
    message: str | None = element(tag='Message', default=None)
    localized_message: str | None = element(tag='LocalizedMessage', default=None)


class Location(BaseXmlModel):
    city: str | None = element(tag='City', default=None)
    state_or_province_code: str | None = element(tag='StateOrProvinceCode', default=None)
    country_code: str | None = element(tag='CountryCode', default=None)
    country_name: str | None = element(tag='CountryName', default=None)
    residential: bool = element(tag='Residential')


class AncillaryDetails(BaseXmlModel, tag='AncillaryDetails'):
    reason: str = element(tag='Reason')
    reason_description: str = element(tag='ReasonDescription')


class StatusDetail(BaseXmlModel):
    creation_time: str | None = element(tag='CreationTime', default=None)
    code: str | None = element(tag='Code', default=None)
    description: str | None = element(tag='Description', default=None)
    location: Location = element(tag='Location')
    ancillary_details: AncillaryDetails | None = element(tag='AncillaryDetails', default=None)


class PackageIdentifier(BaseXmlModel):
    type: str = element(tag='Type')
    value: str = element(tag='Value')


class OtherIdentifiers(BaseXmlModel):
    package_identifier: PackageIdentifier = element(tag='PackageIdentifier')


class Service(BaseXmlModel):
    type: str = element(tag='Type')
    description: str = element(tag='Description')
    short_description: str = element(tag='ShortDescription')


class PackageWeight(BaseXmlModel):
    units: str = element(tag='Units')
    value: float = element(tag='Value')


class PackageDimensions(BaseXmlModel):
    length: int = element(tag='Length')
    width: int = element(tag='Width')
    height: int = element(tag='Height')
    units: str = element(tag='Units')


class ReturnDetail(BaseXmlModel):
    label_type: str = element(tag='LabelType')
    description: str = element(tag='Description')


class SpecialHandlings(BaseXmlModel):
    type: str = element(tag='Type')
    description: str = element(tag='Description')
    payment_type: str = element(tag='PaymentType')


class Payments(BaseXmlModel):
    classification: str = element(tag='Classification')
    type: str = element(tag='Type')
    description: str = element(tag='Description')


class ShipperAddress(BaseXmlModel):
    city: str = element(tag='City')
    state_or_province_code: str = element(tag='StateOrProvinceCode')
    country_code: str = element(tag='CountryCode')
    country_name: str = element(tag='CountryName')
    residential: bool = element(tag='Residential')


class DatesOrTimes(BaseXmlModel, tag='DatesOrTimes'):
    type: str = element(tag='Type')
    date_or_timestamp: str = element(tag='DateOrTimestamp')


class Address(BaseXmlModel):
    city: str = element(tag='City')
    state_or_province_code: str = element(tag='StateOrProvinceCode')
    postal_code: str = element(tag='PostalCode')
    country_code: str = element(tag='CountryCode')
    country_name: str = element(tag='CountryName')
    residential: bool = element(tag='Residential')


class Events(BaseXmlModel):
    timestamp: str = element(tag='Timestamp')
    event_type: str = element(tag='EventType')
    event_description: str = element(tag='EventDescription')
    address: Address = element(tag='Address')
    arrival_location: str = element(tag='ArrivalLocation')


class AvailableImages(BaseXmlModel):
    type: str = element(tag='Type')


class DeliveryOptionEligibilityDetails(BaseXmlModel):
    option: str = element(tag='Option')
    eligibility: str = element(tag='Eligibility')


class ShipmentWeight(BaseXmlModel, tag='ShipmentWeight'):
    units: str = element(tag='Units')
    value: float = element(tag='Value')


class TrackDetails(BaseXmlModel, search_mode='unordered'):
    notification: Notifications = element(tag='Notification')
    tracking_number: str = element(tag='TrackingNumber')
    tracking_number_unique_identifier: str | None = element(tag='TrackingNumberUniqueIdentifier', default=None)
    status_detail: StatusDetail = element(tag='StatusDetail')
    carrier_code: str | None = element(tag='CarrierCode', default=None)
    operating_company_or_carrier_description: str | None = element(
        tag='OperatingCompanyOrCarrierDescription', default=None
    )
    other_identifiers: list[OtherIdentifiers] | None = element(tag='OtherIdentifiers', default=None)
    service: Service | None = element(tag='Service', default=None)
    service_commit_message: str | None = element(tag='ServiceCommitMessage', default=None)
    destination_service_area: str | None = element(tag='DestinationServiceArea', default=None)
    package_weight: PackageWeight | None = element(tag='PackageWeight', default=None)
    package_dimensions: PackageDimensions | None = element(tag='PackageDimensions', default=None)
    shipment_weight: ShipmentWeight | None = element(tag='ShipmentWeight', default=None)
    packaging: str | None = element(tag='Packaging', default=None)
    packaging_type: str | None = element(tag='PackagingType', default=None)
    physical_packaging_type: str | None = element(tag='PhysicalPackagingType', default=None)
    package_sequence_number: int = element(tag='PackageSequenceNumber')
    package_count: int = element(tag='PackageCount')
    return_details: ReturnDetail | None = element(tag='ReturnDetail', default=None)
    special_handlings: SpecialHandlings | None = element(tag='SpecialHandlings', default=None)
    payments: Payments | None = element(tag='Payments', default=None)
    shipper: str | None = element(tag='Shipper', default=None)
    shipper_address: ShipperAddress | None = element(tag='ShipperAddress', default=None)
    original_location_address: ShipperAddress | None = element(tag='OriginLocationAddress', default=None)
    dates_or_times: list[DatesOrTimes] | None = element(tag='DatesOrTimes')
    recipient: str | None = element(tag='Recipient', default=None)
    destination_address: ShipperAddress | None = element(tag='DestinationAddress', default=None)
    actual_delivery_address: ShipperAddress | None = element(tag='ActualDeliveryAddress', default=None)
    delivery_attempts: int | None = element(tag='DeliveryAttempts', default=None)
    delivery_signature_name: str | None = element(tag='DeliverySignatureName', default=None)
    total_unique_address_count_in_consolidation: int | None = element(
        tag='TotalUniqueAddressCountInConsolidation', default=None
    )
    available_images: AvailableImages | None = element(tag='AvailableImages', default=None)
    notification_events_available: str | None = element(tag='NotificationEventsAvailable', default=None)
    delivery_option_eligibility_details: list[DeliveryOptionEligibilityDetails] = element(
        tag='DeliveryOptionEligibilityDetails', default_factory=list
    )
    events: list[Events] | None = element(tag='Events', default=None)


class CompletedTrackDetails(BaseXmlModel):
    highest_severity: str = element(tag='HighestSeverity')
    notifications: Notifications = element(tag='Notifications')
    duplicate_waybill: bool = element(tag='DuplicateWaybill')
    more_data: bool = element(tag='MoreData')
    track_details_count: int = element(tag='TrackDetailsCount', default=0)
    track_details: TrackDetails = element(tag='TrackDetails')


class TrackReply(BaseXmlModel, tag='TrackReply'):
    highest_severity: str = element(tag='HighestSeverity')
    notifications: Notifications = element(tag='Notifications')
    transaction_detail: TransactionDetail = element(tag='TransactionDetail', default_factory=TransactionDetail)
    version: Version = element(tag='Version', default_factory=Version)
    completed_track_details: CompletedTrackDetails = element(
        tag='CompletedTrackDetails', default_factory=CompletedTrackDetails
    )

    @classmethod
    def from_xml(cls, text, *args, **kwargs):
        text = re.sub(' xmlns="[^"]+"', '', text, count=1)
        return super().from_xml(text, *args, **kwargs)
