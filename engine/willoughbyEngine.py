from engine import Engine

class WilloughbyEngine(Engine):
    
    def __init__(self, last_service_mileage, current_milage) -> None:
        self.last_service_mileage = last_service_mileage
        self.current_milage = current_milage
        
    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 60000