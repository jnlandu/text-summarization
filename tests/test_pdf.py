from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test PDF file summarization
def test_summarize_pdf():
    # Open the sample PDF file
    with open("tests/sample.pdf", "rb") as f:
        response = client.post(
            "/summarize/",
            files={"file": ("sample.pdf", f, "application/pdf")},
        )

    # Check if the response status code is 200
    assert response.status_code == 200
    json_response = response.json()
    assert "summary" in json_response
