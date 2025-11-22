class Duties():
    def __init__(self):
        self._duties = []
    
    def add_duty(self, duty):
        for existing_duty in self._duties:
            if existing_duty.number == duty.number:
                return None
        self._duties.append(duty)
        return duty
    
    def get_all_duties(self):
        return self._duties
