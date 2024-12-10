import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Optional

from app.interfaces.email_engine import EmailEngine


class SMTPEmailEngine(EmailEngine):
    """Use this as a context manager"""

    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
        self.server = None

    def __enter__(self):
        try:
            self.server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            # self.server.starttls()
            # self.server.login(self.username, self.password)
            print("SMTP connection established.")
            return self
        except Exception as e:
            print(f"Failed to initialize SMTP connection: {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        if self.server:
            # self.server.quit()
            print("SMTP connection closed.")

    def send_email(
        self, to: str, subject: str, html: Optional[str], body: Optional[str] = None
    ) -> bool:
        if not self.server:
            raise ConnectionError(
                "SMTP connection is not established. Use with a context manager."
            )
        try:
            message = MIMEMultipart("alternative")
            message["From"] = self.username
            message["To"] = to
            message["Subject"] = subject

            if html:
                part = MIMEText(html, "html")
            else:
                part = MIMEText(body, "plain")
            message.attach(part)

            # self.server.sendmail(self.username, to, message.as_string())
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False
