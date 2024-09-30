from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)

# Test text file summarization
def test_summarize_text():
    # Open the sample text file
    with open("tests/sample.txt", "rb") as f:
        response = client.post(
            "/summarize/",
            files={"file": ("sample.txt", f, "text/plain")},
        )
      
    # Check if the response status code is 200
    assert response.status_code == 200
    json_response = response.json()
    assert "summary" in json_response
