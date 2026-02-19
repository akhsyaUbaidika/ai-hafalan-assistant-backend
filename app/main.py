from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.api.router import api_router
from app.core.config import settings
from app.core.logging import setup_logging

setup_logging()

app = FastAPI(
    title=settings.app_name,
    version="1.0.0"
)

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "AI Hafalan Assistant API"}
