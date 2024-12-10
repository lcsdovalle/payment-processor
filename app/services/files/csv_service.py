# app/processors/csv_processor.py
from typing import Generator

import pandas as pd
from fastapi import UploadFile

from app.interfaces.file_processor import FileProcessor


class CSVService(FileProcessor):
    def process_file(self, file: UploadFile, chunk_size=10) -> Generator[pd.DataFrame]:
        """
        This reads a csv in chunks what is more performatic

        Args:
            file (UploadFil): Tje uploaded CSV file.
            chunk_size (int): Number of rows to process per chunk
        Yields:
            pd.DataFrame: A pack of csv rows as a DataFrame
        """
        try:
            for chunk in pd.read_csv(file.file, chunksize=chunk_size, encoding="utf-8"):
                yield chunk
        except Exception as e:
            raise ValueError(f"Error processing CSV: {str(e)}")
