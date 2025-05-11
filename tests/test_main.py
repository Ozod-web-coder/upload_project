import pytest
from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from main import app

@pytest.mark.asyncio
async def test_upload_file_with_auth():
    test_file_content = b"Hello, world!"
    files = {"file": ("test.dcm", test_file_content, "text/plain")}

    valid_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjE3NDY5NDc2NjN9.W2PW9h43mAtrsiHVGKrtPIGfLCgf6-4uUKLk9IUVuTs"

    with TestClient(app) as client:
        response = client.post(
            "/upload/",
            files=files,
            headers={"Authorization": f"Bearer {valid_token}"}
        )

    assert response.status_code == 200
