from fastapi import APIRouter, Request
from backend.app.utils.gpt import get_gpt_response

chat_router = APIRouter()

@chat_router.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("message", "")
    response = await get_gpt_response(user_input)
    return {"response": response}
