import pytest
from app import app
import warnings
warnings.filterwarnings("ignore")

@pytest.fixture
def client():
    return app.test_client()

def testServerActiveMethod(client):
    response = client.get('/serveractive')
    assert response.status_code == 200
    assert response.json == {'Success' : 'Server is Active. Congrats'}