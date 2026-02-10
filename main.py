from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, List
from typing import Optional
import uuid
from supabase import create_client, Client
import os

SUPABASE_URL = "https://csmatcjemdqrpsuefvwf.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNzbWF0Y2plbWRxcnBzdWVmdndmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzAxODYyOTcsImV4cCI6MjA4NTc2MjI5N30.TBO2Lab1c65BOCR5G-jf9dDFKI4Xhq1PBgxSG6tuzNY"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


app = FastAPI()

@app.get("/supabase-test")
def supabase_test():
    data = supabase.table("conversation").select("*").limit(1).execute()
    return {
        "connected": True,
        "data": data.data
    }



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









    


