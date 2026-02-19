from fastapi import APIRouter
from app.repositories.santri_repository import SantriRepository

router = APIRouter()

@router.get("/santri")
def get_all_santri():
    data = SantriRepository.get_all_santri()
    return {
        "status": "success",
        "total": len(data),
        "data": data
    }
