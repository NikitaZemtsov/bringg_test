from abc import ABC, abstractmethod


class CarrierAPI(ABC):
    @abstractmethod
    def track(self, *args, **kwargs):
        pass
