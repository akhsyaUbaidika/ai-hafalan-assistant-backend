from fastapi import APIRouter
from app.api.routes import health, santri, hafalan, chat, insight


api_router = APIRouter()

api_router.include_router(health.router, tags=["Health"])
api_router.include_router(santri.router, tags=["Santri"])
api_router.include_router(hafalan.router, tags=["Hafalan"])
api_router.include_router(chat.router, tags=["AI Chat"])
api_router.include_router(insight.router, tags=["AI Insight"])
