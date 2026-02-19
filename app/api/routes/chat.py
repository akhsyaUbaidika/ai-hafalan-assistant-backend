from fastapi import APIRouter
from pydantic import BaseModel
from app.services.chat_service import ChatService

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(request: ChatRequest):
    answer = ChatService.ask_ai(request.message)

    return {
        "status": "success",
        "answer": answer
    }
