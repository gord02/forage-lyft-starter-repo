import unittest
from datetime import datetime
import sys

sys.path.insert(0,'..')

from battery import nubbinBattery
from battery import spindlerBattery

from engine import capuletEngine
from engine import sternmanEngine
from engine import willoughbyEngine

from tire import carriganTire
from tire import octoprimeTire


class TestCapuletEngine(unittest.TestCase):
    
    def test_does_not_need_serivce(self):
        last_service_mileage = 0
        current_milage = 0
        test_engine = capuletEngine.CapuletEngine(last_service_mileage, current_milage)
        self.assertFalse(test_engine.needs_service())
        
    def test_needs_serivce(self):
        last_service_mileage = 0
        current_milage = 30001
        test_engine = capuletEngine.CapuletEngine(last_service_mileage, current_milage)
        self.assertTrue(test_engine.needs_service())
        
class TestWilloughbyEngine(unittest.TestCase):
    
    def test_does_not_need_serivce(self):
        last_service_mileage = 0
        current_milage = 0
        test_engine = willoughbyEngine.WilloughbyEngine(last_service_mileage, current_milage)
        self.assertFalse(test_engine.needs_service())
        
    def test_needs_serivce(self):
        last_service_mileage = 0
        current_milage = 60001
        test_engine = willoughbyEngine.WilloughbyEngine(last_service_mileage, current_milage)
        self.assertTrue(test_engine.needs_service())
        
class TestSternmanEngine(unittest.TestCase):
    
    def test_does_not_need_serivce(self):
        warning_light_is_on = False
        test_engine = sternmanEngine.SternmanEngine(warning_light_is_on)
        self.assertFalse(test_engine.needs_service())
        
    def test_needs_serivce(self):
        warning_light_is_on = True
        test_engine = sternmanEngine.SternmanEngine(warning_light_is_on)
        self.assertTrue(test_engine.needs_service())
        
        
class TestNubbinBattery(unittest.TestCase):
    def test_does_not_need_serivce(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        test_battery = nubbinBattery.NubbinBattery(last_service_date, today)
        self.assertFalse(test_battery.needs_service())
        
    def test_needs_serivce(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        test_battery = nubbinBattery.NubbinBattery(last_service_date, today)
        self.assertTrue(test_battery.needs_service())
        
class TestSpindlerBattery(unittest.TestCase):
    def test_does_not_need_serivce(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        test_battery = spindlerBattery.SpindlerBattery(last_service_date, today)
        self.assertFalse(test_battery.needs_service())
        
    def test_needs_serivce(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        test_battery = spindlerBattery.SpindlerBattery(last_service_date, today)
        self.assertTrue(test_battery.needs_service())
        
class TestCarriganTire(unittest.TestCase): 

    def test_does_not_need_service(self):
        tires = carriganTire.CarriganTire([0.1, 0.7, 0.5,0.85])
        self.assertFalse(tires.needs_service())

    def test_needs_service(self):
        tires = carriganTire.CarriganTire([1, 0.7, 0.5,1])
        self.assertTrue(tires.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    
    def test_does_not_need_service(self):
        tires = octoprimeTire.OctoprimeTire([0.2, 0.3, 0.5,0.3])
        self.assertFalse(tires.needs_service())
        
    def test_needs_service(self):
        tires = octoprimeTire.OctoprimeTire([1, 0.7, 0.5,1])
        self.assertTrue(tires.needs_service())
        
if __name__ == '__main__':
    unittest.main(verbosity=2)