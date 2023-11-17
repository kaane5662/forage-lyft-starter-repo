from abc import ABC, abstractmethod
from Engine import Engine
from Battery import Battery
from Servicable import Servicable

class Car(Servicable):
    
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.Engine:Engine
        self.Battery: Battery

    def needs_service(self):
        return self.Engine.needs_service() | self.Battery.needs_service()
    
    
    


