# app/dependencies/auth.py
from fastapi import Security
from fastapi.security import APIKeyHeader
from app.config.settings import settings

API_KEY = settings.API_KEY
API_KEY_NAME = settings.API_KEY_NAME

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


def get_authenticated_user(api_key: str = Security(api_key_header)):
    return {"user": "fake_user", "role": "admin"}
