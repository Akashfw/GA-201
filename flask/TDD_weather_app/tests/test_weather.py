import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_weather(client):
    response = client.get('/weather/San Francisco')
    data = response.get_json()

    assert response.status_code == 200
    assert data == {'temperature': 14, 'weather': 'Cloudy'}

def test_add_weather(client):
    response = client.post('/weather', json={'city': 'Boston', 'temperature': 18, 'weather': 'Cloudy'})
    data = response.get_json()

    assert response.status_code == 200
    assert data == {'message': 'Weather data added successfully.'}

def test_update_weather(client):
    response = client.put('/weather/Seattle', json={'temperature': 12})
    data = response.get_json()

    assert response.status_code == 200
    assert data == {'message': 'Weather data updated successfully.'}

def test_delete_weather(client):
    response = client.delete('/weather/Austin')
    data = response.get_json()

    assert response.status_code == 200
    assert data == {'message': 'Weather data deleted successfully.'}
