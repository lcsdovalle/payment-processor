from abc import ABC, abstractmethod
from typing import Generator

from fastapi import UploadFile


class FileProcessor(ABC):
    @abstractmethod
    def process_file(self, file: UploadFile) -> Generator:
        """Process the given file and return a result summary."""
        pass
