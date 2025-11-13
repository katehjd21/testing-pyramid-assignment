from models.db import Db
from models.duty import Duty
import pytest

@pytest.fixture
def create_duty():
    return Duty("Random Duty", "", "")


def test_user_can_save_duty(mocker, create_duty):
    mocked_save = mocker.patch("models.db.Db.save", return_value=True)
    assert Db.save(create_duty) == True
    assert mocked_save.call_count == 1
    mocked_save.assert_called_with(create_duty)


def test_user_can_read_all_duties(mocker, create_duty):
    mocker.patch("models.db.Db.list_all_duties", return_value=[create_duty])
    assert Db.list_all_duties() == [create_duty]

def test_user_can_read_a_single_duty_by_id(mocker, create_duty):
    mocker.patch("models.db.Db.read", return_value=create_duty)
    assert Db.read() == create_duty

