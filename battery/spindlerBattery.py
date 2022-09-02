from battery.battery import Battery

class SpindlerBattery(Battery):
    
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        
    
    def needs_service(self):
        time = self.current_date.year - self.last_service_date.year
        if time > 2:
            return True
        return False