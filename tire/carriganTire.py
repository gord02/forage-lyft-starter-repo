from tire.tireModel import Tire

class CarriganTire(Tire):
    
    def __init__(self, tireGrades):
        self.tireGrades = tireGrades
        
    def needs_service(self):
        for grade in self.tireGrades:
            if grade > 0.9:
                return True
        return False