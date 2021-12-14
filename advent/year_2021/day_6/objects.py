

class Latenfish:

    def __init__(self, days_left: int):
        self.days = days_left
    
    def lower_days(self):
        self.days -= 1
    
    def reset(self):
        self.days = 6
