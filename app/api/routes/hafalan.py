from fastapi import APIRouter
from app.repositories.hafalan_repository import HafalanRepository

router = APIRouter()

@router.get("/hafalan")
def get_hafalan(bulan: str, tahun: str):
    data = HafalanRepository.get_hafalan_by_periode(bulan, tahun)
    return {
        "status": "success",
        "total": len(data),
        "data": data
    }
