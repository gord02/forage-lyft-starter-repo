from battery import Battery

class NubbinBattery(Battery):
    
    def __init__(self, lasst_service_date:int, current_date: int) -> None:
        self.lasst_service_date = lasst_service_date
        self.current_date = current_date
    
    def needs_service(self) -> bool:
        pass