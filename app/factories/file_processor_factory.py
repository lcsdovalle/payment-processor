from fastapi import UploadFile

from app.exceptions.files import UnsupportedFileTypeException
from app.interfaces.file_processor import FileProcessor
from app.services.files.csv_service import CSVService


class ProcessorFactory:
    @staticmethod
    def get_processor(file: UploadFile) -> FileProcessor:
        if file.content_type == "text/csv":
            return CSVService()
        raise UnsupportedFileTypeException(
            f"Unsupported file type: {file.content_type}"
        )
