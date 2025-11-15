class Duties():
    def __init__(self):
        self._duties = []
    
    def add_duty(self, duty):
        self._duties.append(duty)
        return duty
    
    def get_all_duties(self):
        return self._duties
