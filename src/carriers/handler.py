from .carrier import Carrier
from .fedex import FedEx, FedExAPI


class CarrierHandler:
    def __init__(self, carriers):
        self.carriers: dict[str, Carrier] = carriers


fedex: FedEx = FedEx(api=FedExAPI(), api_url='https://wsbeta.fedex.com:443/xml/track/v14')

carrier_handler = CarrierHandler(carriers={fedex.name: fedex})
