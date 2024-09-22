from .carrier import Carrier
from .fedex.fedex import fedex


class CarrierHandler:
    def __init__(self, carriers):
        self.carriers: dict[str, Carrier] = carriers


carrier_handler = CarrierHandler(carriers={fedex.name: fedex})
