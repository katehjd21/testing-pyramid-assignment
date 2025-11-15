import pytest
from models.duties import Duties
from models.duty import Duty
from controllers.duties_controller import DutiesController, duties_store

@pytest.fixture
def duty():
    return Duty("Duty 1", "Test Description", ["Knowledge", "Skills", "Behaviours"])

@pytest.fixture
def duties_controller():
    return DutiesController()

@pytest.fixture
def list_of_duties():
    return Duties().get_all_duties()

def test_duties_controller_can_fetch_all_duties(mocker, list_of_duties, duties_controller):
    mocked_get_all_duties = mocker.patch.object(duties_store, "get_all_duties", return_value=list_of_duties)
    fetched_list_of_duties = duties_controller.fetch_all_duties()
    assert mocked_get_all_duties.call_count == 1
    assert fetched_list_of_duties == list_of_duties
    assert len(fetched_list_of_duties) == len(list_of_duties)

def test_duties_controller_can_add_a_duty_to_the_duties_store(mocker, duties_controller, duty):
    mocked_add_duty = mocker.patch.object(duties_store, "add_duty", side_effect=lambda d: d)
    created_duty = duties_controller.create_duty("2", "Other Duty Description", ["Knowledge", "Skills", "Behaviours"])
    assert mocked_add_duty.call_count == 1
    assert created_duty.number == "2"
    assert created_duty.description == "Other Duty Description"
    assert created_duty.ksbs == ["Knowledge", "Skills", "Behaviours"]
    assert created_duty.complete is False


