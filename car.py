from abc import ABC, abstractmethod
from Engine import Engine
from Battery import Battery
from Servicable import Servicable
from TireService import TireService

class Car(Servicable, TireService):
    
    def __init__(self, Engine, Battery):
        self.Engine = Engine
        self.Battery = Battery
        self.Tires = [0,0,0,0]

    def needs_service(self):
        return self.Engine.needs_service() or self.Battery.needs_service()
    
    def check_tire_wear(self):
        sum = 0
        for tire_wear in self.Tires:
            sum += tire_wear
        if sum >= 3:
            return "Octoprime"
        for tire_wear in self.Tires:
            if(tire_wear >= .9):
                return "Carrigan"


