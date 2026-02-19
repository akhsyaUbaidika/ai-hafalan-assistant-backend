from fastapi import APIRouter
from datetime import datetime
from app.services.insight_service import InsightService

router = APIRouter()


@router.get("/insight")
def get_insight(bulan: str, tahun: str):

    result = InsightService.generate_monthly_insight(bulan, tahun)

    return {
        "status": "success",
        "generated_at": datetime.utcnow(),
        "insight": result
    }
