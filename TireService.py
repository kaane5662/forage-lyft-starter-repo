from abc import ABC, abstractmethod

class TireService(ABC):
    @abstractmethod
    def check_tire_wear():
        pass