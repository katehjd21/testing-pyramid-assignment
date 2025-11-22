import pytest
from app import app
from controllers.duties_controller import duties_store

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_automate_duties_page_post_duties(client):
    duties_store._duties.clear()

    response = client.post('/automate', data={
        'number': '1',
        'description': 'Duty 1 Description',
        'ksbs': 'Knowledge, Skills, Behaviours'
    }, follow_redirects=True)

    html = response.data.decode()
    assert response.status_code == 200

    all_duties = duties_store.get_all_duties()
    for duty in all_duties:
        assert f"<td>{duty.number}</td>" in html
        assert f"<td>{duty.description}</td>" in html
        assert f"<td>{', '.join(duty.ksbs)}</td>" in html


def test_automate_duties_page_post_duties_with_empty_description(client):
    duties_store._duties.clear()
    response = client.post('/automate', data={
        'number': '1',
        'description': '',
        'ksbs': 'K, S, B'
    }, follow_redirects=True)

    html = response.data.decode()

    assert response.status_code == 200

    all_duties = duties_store.get_all_duties()
    for duty in all_duties:
        assert f"<td>{duty.number}</td>" in html
        assert f"<td>{duty.description}</td>" in html
        assert f"<td>{', '.join(duty.ksbs)}</td>" in html