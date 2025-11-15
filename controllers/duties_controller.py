from models.duties import Duties
from models.duty import Duty

duties_store = Duties()

class DutiesController():

    @staticmethod
    def fetch_all_duties():
        return duties_store.get_all_duties()
    
    @staticmethod
    def create_duty(number, description, ksbs):
        duty = Duty(number, description, ksbs)
        return duties_store.add_duty(duty)
