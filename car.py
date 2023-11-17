from abc import ABC, abstractmethod
from Engine import Engine
from Battery import Battery
from Servicable import Servicable

class Car(Servicable):
    
    def __init__(self, Engine, Battery):
        self.Engine = Engine
        self.Battery = Battery

    def needs_service(self):
        return self.Engine.needs_service() or self.Battery.needs_service()
    
    
    


