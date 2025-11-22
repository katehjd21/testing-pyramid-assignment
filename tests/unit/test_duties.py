import pytest
from models.duties import Duties
from models.duty import Duty

@pytest.fixture
def duties():
    return Duties()

@pytest.fixture
def duty1():
    return Duty(1, "Test description 1", ["Knowledge", "Skills", "Behaviours"])

@pytest.fixture
def duty2():
    return Duty(2, "Test description 2", ["Knowledge", "Skills", "Behaviours"])

def test_add_duty(duties, duty1):
    assert duties.add_duty(duty1) == duty1
    assert duties.get_all_duties() == [duty1]

def test_add_multiple_unique_duties(duties, duty1, duty2):
    added_duty_1 = duties.add_duty(duty1)
    added_duty_2 = duties.add_duty(duty2)
    assert duties.get_all_duties() == [added_duty_1, added_duty_2]

def test_add_duty_ensures_no_duties_have_same_number(duties, duty1):
    added_duty_1 = duties.add_duty(duty1)
    duplicate_duty = duties.add_duty(duty1)
    assert duplicate_duty == None
    assert duties.get_all_duties() == [added_duty_1]

def test_duplicate_number_with_different_description(duties, duty1):
    duty1_different_description = Duty(1, "Different description", ["K1", "S1", "B1"])
    duties.add_duty(duty1)
    assert duties.add_duty(duty1_different_description) is None
    assert duties.get_all_duties() == [duty1]

def test_get_all_duties(duties, duty1):
    duties.add_duty(duty1)
    assert duties.get_all_duties() == [duty1]

