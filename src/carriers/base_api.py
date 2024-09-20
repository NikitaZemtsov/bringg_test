from abc import ABC, abstractmethod


class CarriersAPI(ABC):
    @abstractmethod
    def track(self, track_number: str):
        pass
