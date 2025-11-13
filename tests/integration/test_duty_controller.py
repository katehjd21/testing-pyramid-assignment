from models.db import Db
from models.duty import Duty
from controllers.duty import DutyController

duty = Duty("", "", "")
duty_controller = DutyController()

def test_controller_can_save_duty(mocker):
    mocker_saved = mocker.patch("models.duty.Duty.save", return_value=True)
    duty_controller.save(duty)
    assert mocker_saved.call_count == 1
