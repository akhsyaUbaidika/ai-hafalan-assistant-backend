from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.utcnow()
    }

@router.get("/version")
def version():
    return {
        "app": "AI Hafalan Assistant API",
        "version": "1.0.0",
        "environment": "development"
    }
