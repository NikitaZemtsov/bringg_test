from abc import ABC, abstractmethod


class Carrier(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def track(self, track_number):
        pass
