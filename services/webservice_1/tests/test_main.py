from collections import Counter

from fastapi.testclient import TestClient

from src.main import app


def test_randomness():
    client = TestClient(app)

    results = [client.get("/play", params={"a": "rock"}).json() for _ in range(100)]

    counts = Counter(results)
    assert 20 <= counts[True] <= 40
