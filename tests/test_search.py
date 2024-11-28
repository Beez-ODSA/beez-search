import pytest
from fastapi.testclient import TestClient
from app.main import app

# Initialize the test client
client = TestClient(app)

def test_root_endpoint():
    """
    Test the root endpoint to ensure it's working correctly.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Search service is running"}  # Update based on your actual app response

def test_search_endpoint():
    """
    Test the search endpoint to ensure it handles valid requests.
    """
    payload = {"query": "example search"}
    response = client.post("/search", json=payload)
    assert response.status_code == 200
    assert "results" in response.json()

def test_invalid_search_payload():
    """
    Test the search endpoint with invalid payloads to ensure proper error handling.
    """
    payload = {"invalid_field": "test"}
    response = client.post("/search", json=payload)
    assert response.status_code == 422  # Unprocessable Entity (FastAPI validation)

@pytest.mark.parametrize(
    "query,expected_status_code",
    [
        ("valid query", 200),  # Test valid search
        ("", 422),            # Empty query (validation should fail)
    ],
)
def test_search_query_validation(query, expected_status_code):
    """
    Test search query validation with various inputs.
    """
    payload = {"query": query}
    response = client.post("/search", json=payload)
    assert response.status_code == expected_status_code