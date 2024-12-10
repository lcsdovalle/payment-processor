from typing import Optional

from pydantic import EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

env_path = Path(__file__).parent.parent / ".env"
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=env_path)
    
    # Application Settings
    APP_NAME: str = "External Services"
    ENV: str = "development"  # Values: development, production, testing
    DEBUG: bool = True

    # Email Settings
    SMTP_SERVER: Optional[str] = None
    SMTP_PORT: Optional[int] = None
    SMTP_USERNAME: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    ADMIN_EMAIL: Optional[EmailStr | None] = None

    # Payment Settings
    STRIPE_API_KEY: Optional[str] = None
    PAGBANK_API_KEY: Optional[str] = None
    PAYPALL_API_KEY: Optional[str] = None

    API_KEY: Optional[str] = None
    API_KEY_NAME: Optional[str] = None

    DEFAULT_API_VERSION: Optional[str] = "/api/v1"

settings = Settings()
