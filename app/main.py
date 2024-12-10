# app/main.py
from fastapi import FastAPI

from app.routers import payment
from app.config.settings import settings
app = FastAPI()

app.include_router(payment.router, prefix=settings.DEFAULT_API_VERSION)
