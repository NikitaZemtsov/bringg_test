from base_api import CarriersAPI

from .fedex import FedExAPI


class CarrierHandler:
    def __init__(self, carriers):
        self.carriers: dict[str, CarriersAPI] = carriers

    def track(self, carrier_name: str, tracking_number: str):
        track_data = None
        if carrier := self.carriers.get(carrier_name):
            track_data = carrier.track(track_number=tracking_number)
        return track_data


carrier_handler = CarrierHandler(carriers={'fedex': FedExAPI})
