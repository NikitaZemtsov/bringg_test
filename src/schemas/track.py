import enum
from datetime import datetime

from pydantic import BaseModel


class Locale(enum.StrEnum):
    en_us = 'en_US'


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


class Checkpoint(BaseModel):
    description: str
    status: str
    tracking_stage: str
    time: datetime


class TrackSuccessfulResponse(BaseModel):
    carrier: str
    checkpoints: list[Checkpoint] = []
    delivered: bool | None
    delivery_date: datetime | None = None
    estimated_delivery: datetime | None = None
    locale: Locale | None = None
    status: str | None = None
    tracking_number: str
    tracking_stage: TrackingStage | None = None
