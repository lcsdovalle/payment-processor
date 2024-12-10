# app/interfaces/email_engine.py
from abc import ABC, abstractmethod


class EmailEngine(ABC):
    @abstractmethod
    def send_email(self, to: str, subject: str, body: str) -> bool:
        """
        Sends an email.

        Args:
            to (str): Recipient email address.
            subject (str): Email subject line.
            body (str): Email body content.

        Returns:
            bool: True if the email was sent successfully, False otherwise.
        """
        pass
