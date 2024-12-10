# tests/test_factories.py
from io import BytesIO

import pytest
from fastapi import UploadFile

from app.exceptions.files import UnsupportedFileTypeException
from app.factories.file_processor_factory import ProcessorFactory
from app.services.files.csv_service import CSVService


def test_get_csv_processor(csv_upload_file):
    processor = ProcessorFactory.get_processor(csv_upload_file)
    assert isinstance(processor, CSVService)


def test_unsupported_file_type(csv_file_content_and_name):
    FILE_TYPE = "text/plain"
    file_content, file_name = csv_file_content_and_name
    file = UploadFile(
        filename=file_name,
        file=BytesIO(file_content),
        headers={"content-type": FILE_TYPE},
    )
    with pytest.raises(UnsupportedFileTypeException) as exec:
        ProcessorFactory.get_processor(file)
    isinstance(exec.value, UnsupportedFileTypeException)
