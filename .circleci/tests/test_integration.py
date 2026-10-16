
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "ok"
    assert data["postgres"] is True
    assert data["redis"] is True


def test_quizzes_endpoint():
    response = client.get("/quizzes")
    assert response.status_code == 200

    data = response.json()
    assert "quizzes" in data
    assert isinstance(data["quizzes"], list)
