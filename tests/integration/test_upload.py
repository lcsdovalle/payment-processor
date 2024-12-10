import pytest
from fastapi.testclient import TestClient

from app.helpers.constants import FILE_UPLOAD_ERROR_MESSAGE
from app.exceptions.files import UnsupportedFileTypeException
from app.main import app


def make_request(endpoint_url, request_files, client: TestClient):
    return client.post(endpoint_url, files=request_files)


@pytest.mark.parametrize(
    "dynamic_file_content_and_name",
    [
        {"headers": {"Content-Type": "text/csv"}},  # Supported
        {"headers": {"Content-Type": "text/plain"}},  # Unsupported
    ],
    indirect=True,
)
def test_file_type_validation(dynamic_file_content_and_name):
    client = TestClient(app)
    ENDPOINT_URL = "/payment/bulk/"
    content, file_name, headers, _ = dynamic_file_content_and_name

    request_files = {"file": (file_name, content, headers["Content-Type"])}

    if headers["Content-Type"] == "text/csv":
        response = make_request(ENDPOINT_URL, request_files, client)
        assert response.status_code == 200
        assert "Payments processed" in response.json().get("Result", "")
    else:
        with pytest.raises(UnsupportedFileTypeException) as exec:
            response = make_request(ENDPOINT_URL, request_files, client)
            assert response.status_code == 400
            assert response.json()["detail"] == FILE_UPLOAD_ERROR_MESSAGE
        assert isinstance(exec.value, UnsupportedFileTypeException)
