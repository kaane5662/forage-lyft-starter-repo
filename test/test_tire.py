import unittest

from battery.SpindlerBattery import SpindlerBattery
from battery.NubbinBattery import NubbinBattey

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from car import Car
class test_tire(unittest.TestCase):


    def test_tire_wear_Carrigan(self):
        car1 = Car(Engine=CapuletEngine(0,0,0), Battery=NubbinBattey(0,0))
        car1.Tires = [0.9,0.9,0.9,0.9]
        self.assertTrue(car1.check_tire_wear(), None)
        car1.Tires = [0.7,.6,.9,.3]
        self.assertTrue(car1.check_tire_wear(), "Carrigan")
        car1.Tires = [0,.6,.80,.45]
        # self.assertTrue(car1.check_tire_wear(), "Octoprime")
        car1.Tires = [.9,.5,.4,.3]
        self.assertEqual(car1.check_tire_wear(), "Carrigan") 
    
    def test_tire_wear_Octoprime(self):
        car1 = Car(Engine=CapuletEngine(0,0,0), Battery=NubbinBattey(0,0))
        car1.Tires = [0.9,0.9,0.9,0.9]
        self.assertEqual(car1.check_tire_wear(), "Octoprime")
        car1.Tires = [0.8,.8,.8,.8]
        self.assertEqual(car1.check_tire_wear(), "Octoprime")
        car1.Tires = [0,.6,.80,.45]
        self.assertFalse(car1.check_tire_wear(), "Octoprime")
        car1.Tires = [.9,1,1,1]
        self.assertEqual(car1.check_tire_wear(), "Octoprime") 
