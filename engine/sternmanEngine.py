from engine.engineModel import EngineModel

class SternmanEngine(EngineModel):
    
    def __init__(self, warning_light_on: bool):
        self.warning_light_on = warning_light_on
    
    def needs_service(self): 
        if self.warning_light_on:
                return True
        else:
            return False