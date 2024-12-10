from io import BytesIO
from pathlib import Path

import pytest
from fastapi import UploadFile


@pytest.fixture
def csv_file():
    """This returns a CSv to be used in the tests"""
    fixtures_dir = Path(__file__).parent.parent / "fixtures"
    file_path = fixtures_dir / "test_data.csv"
    print("FILE_PATH", file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"File doesn't exis {file_path}")

    yield file_path


@pytest.fixture
def csv_file_content_and_name(csv_file):
    with open(csv_file, "rb") as file:
        file_content = file.read()
    yield file_content, csv_file
    file.close()


@pytest.fixture
def csv_upload_file(csv_file_content_and_name):
    file_content, file_name = csv_file_content_and_name
    yield UploadFile(
        filename=file_name,
        file=BytesIO(file_content),
        headers={"content-type": "text/csv"},
    )


@pytest.fixture
def dynamic_file_content_and_name(request, csv_file_content_and_name):
    """
    Fixture to provide file content, name, headers, and other dynamic parameters.
    This fixtgure receives params dinamically so that tests can easily mock a failure, for instance
    """
    headers = request.param.get("headers", {"Content-Type": "text/csv"})
    additional_param = request.param.get("additional_param", None)
    content, file_path = csv_file_content_and_name
    yield content, str(file_path), headers, additional_param
