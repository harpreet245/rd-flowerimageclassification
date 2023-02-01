import pytest
from app import app
import warnings
from werkzeug.datastructures import FileStorage
import io
warnings.filterwarnings("ignore")

@pytest.fixture
def client():
    return app.test_client()

def testPredictionMethod(client):
    fileName1 = "flowerData/roses/110472418_87b6a3aa98_m.jpg"
    fileName2 = "flowerData/tulips/65347450_53658c63bd_n.jpg"
    dataFile1 = {'fileUpload' : (open(fileName1, 'rb'), "110472418_87b6a3aa98_m.jpg")}
    dataFile2 = {'fileUpload' : (open(fileName2, 'rb'), "65347450_53658c63bd_n.jpg")}
    response1 = client.post('/predictionpytest', data = dataFile1, buffered=True, content_type="multipart/form-data")
    response2 = client.post('/predictionpytest', data = dataFile2, buffered=True, content_type="multipart/form-data")
    assert response1.status_code == 200
    assert response1.json == {'FlowerType' : "roses"}
    assert response2.status_code == 200
    assert response2.json == {'FlowerType' : "tulips"}