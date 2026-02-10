from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, List
from typing import Optional
import uuid
from supabase import create_client, Client
import os



app = FastAPI()


class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[str] = None


class ChatResponse(BaseModel):
    conversation_id: str
    response: str


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # create conversation id if frontend doesn't send one
    conversation_id = request.conversation_id or str(uuid.uuid4())

    # temporary fake response
    fake_response = f"You said: '{request.message}'. UC Davis chatbot coming soon."

    return ChatResponse(
        conversation_id=conversation_id,
        response=fake_response
    )









    


