import unittest

from battery.SpindlerBattery import SpindlerBattery
from battery.NubbinBattery import NubbinBattey

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from car import Car
class test_car_2(unittest.TestCase):
    def test_callilope(self):
        callilope = Car(Engine=CapuletEngine(0,0,0), Battery=SpindlerBattery(0,0))
        callilope.Engine.current_mileage = 30001
        self.assertTrue(callilope.Engine.needs_service())
        callilope.Battery.current_date = 3
        self.assertTrue(callilope.Battery.needs_service())
        self.assertTrue(callilope.needs_service())

    def test_glissade(self):
        glissade = Car(Engine=WilloughbyEngine(0,0,0), Battery=SpindlerBattery(0,0))
        glissade.Engine.current_mileage = 600001
        self.assertTrue(glissade.Engine.needs_service())
        glissade.Battery.current_date = 3
        # self.assertTrue(glissade.Battery.needs_service())
        self.assertTrue(glissade.needs_service())

    def test_palindrom(self):
        palindrome = Car(Engine=SternmanEngine(0,0,0), Battery=SpindlerBattery(0,0))
        palindrome.Engine.warning_light_is_on = True
        self.assertTrue(palindrome.Engine.needs_service())
        palindrome.Battery.current_date = 3
        palindrome.Engine.warning_light_is_on = False
        self.assertFalse(palindrome.Engine.needs_service())
        self.assertTrue(palindrome.Battery.needs_service())
        self.assertTrue(palindrome.needs_service())

    def test_rorschach(self):
        rorschach = Car(Engine=WilloughbyEngine(0,0,0), Battery=NubbinBattey(0,0))
        rorschach.Engine.current_mileage = 30
        self.assertFalse(rorschach.Engine.needs_service())
        rorschach.Battery.current_date = 5
        self.assertFalse(rorschach.Engine.needs_service())
        self.assertFalse(rorschach.needs_service())
        
    def test_thovex(self):
        thovex = Car(Engine=CapuletEngine(0,0,0), Battery=NubbinBattey(0,0))
        thovex.Engine.current_mileage = 25000
        self.assertFalse(thovex.Engine.needs_service())
        thovex.Battery.current_date = 3
        self.assertFalse(thovex.Engine.needs_service())
        self.assertFalse(thovex.needs_service())