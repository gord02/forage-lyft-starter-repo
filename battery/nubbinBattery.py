from battery.battery import Battery
from datetime import datetime


class NubbinBattery(Battery):
    
    def __init__(self, last_service_date: datetime, current_date: datetime):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self):
        time = self.current_date.year - self.last_service_date.year
        if  time > 3:
            return True
        return False