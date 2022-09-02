from tire.tireModel import Tire

class OctoprimeTire(Tire):
    
    def __init__(self, tireGrades):
        self.tireGrades = tireGrades
        
    def needs_service(self):
        tireWear = 0.0
        for grade in self.tireGrades:
            tireWear += grade
        
        if tireWear >= 3.0:
            return True
        
        return False