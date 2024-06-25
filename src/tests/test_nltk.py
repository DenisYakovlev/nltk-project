from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

# Example input text for testing
input_text = "Hello, this is the basic test. London, Germany, Italy."


def test_tokenize_endpoint():
    # Test /tokenize endpoint
    response = client.post("/tokenize/", json={"text": input_text})
    assert response.status_code == 200
    assert "tokens" in response.json()


def test_pos_tag_endpoint():
    # Test /pos_tag endpoint
    response = client.post("/pos_tag/", json={"text": input_text})
    assert response.status_code == 200
    assert "tagged_tokens" in response.json()


def test_ner_endpoint():
    # Test /ner endpoint
    response = client.post("/ner/", json={"text": input_text})
    assert response.status_code == 200
    assert "named_entities" in response.json()
