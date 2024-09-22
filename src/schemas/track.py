import enum
from datetime import datetime

from pydantic import BaseModel


class Locale(enum.StrEnum):
    EN_US = 'en_US'


class TrackingStage(enum.StrEnum):
    CREATION_PENDING = 'CREATION_PENDING'
    CREATED = 'CREATED'
    PICKED_UP = 'PICKED_UP'
    IN_TRANSIT = 'IN_TRANSIT'
    OUT_FOR_DELIVERY = 'OUT_FOR_DELIVERY'
    DRIVER_ASSIGNED = 'DRIVER_ASSIGNED'
    CHECKED_IN = 'CHECKED_IN'
    DELIVERED = 'DELIVERED'
    SHIPMENT_VOIDED = 'SHIPMENT_VOIDED'
    EXCEPTION = 'EXCEPTION'


class ErrorCode(enum.StrEnum):
    CARRIER_TIMEOUT = 'carrier_timeout'
    UNEXPECTED_EXCEPTION = 'unexpected_exception'
    CARRIER_AUTHENTICATION = 'carrier_authentication'
    SCHEMA_FIELD_REQUIRED = 'schema_field_required'
    CARRIER_FAILED_CONNECTION = 'carrier_failed_connection'
    CARRIER_UNSUPPORTED_METHOD = 'carrier_unsupported_method'
    CARRIER_NO_SHIPMENT_FOUND = 'carrier_no_shipment_found'
    WRONG_API_KEY = 'wrong_api_key'
    CARRIER_HTTP_EXCEPTION = 'carrier_http_exception'
    CARRIER_THROTTLING = 'carrier_throttling'
    SHIPPING_ACCOUNT_WRONG_CARRIER = 'shipping_account_wrong_carrier'
    SHIPPING_ACCOUNT_NOT_FOUND = 'shipping_account_not_found'
    CARRIER_EXCEPTION = 'carrier_exception'
    MISSING_API_KEY = 'missing_api_key'
    SCHEMA_VALIDATION_ERROR = 'schema_validation_error'


class Checkpoint(BaseModel):
    description: str
    status: str
    tracking_stage: str
    time: datetime


class TrackSuccessfulResponse(BaseModel):
    carrier: str
    checkpoints: list[Checkpoint] = []
    delivered: bool | None = None
    delivery_date: datetime | None = None
    estimated_delivery: datetime | None = None
    locale: Locale | None = None
    status: str | None = None
    tracking_number: str
    tracking_stage: TrackingStage | None = None


class TrackErrorResponse(BaseModel):
    code: ErrorCode
    detail: str | None = ''
    message: str | None = ''
