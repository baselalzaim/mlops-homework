import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_predict_endpoint_responds(client):
    response = client.get("/predict?text=hello")
    assert response.status_code == 200


def test_predict_endpoint_with_different_inputs(client):
    test_inputs = ["hello", "world", "mlops", "test123"]
    for text in test_inputs:
        response = client.get(f"/predict?text={text}")
        assert response.status_code == 200
        data = response.json()
        assert "prediction" in data
        assert isinstance(data["prediction"], (int, float))
