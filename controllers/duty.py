from models.duty import Duty

class DutyController:

    def save(self, duty):
        Duty("", "", "").save()

    @staticmethod
    def get_duty():
        return Duty.get_duty()