from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, List
import uuid


app = FastAPI()

#defines the shape of the incoming request
class ChatRequest(BaseModel):
    message: str
    conversation_id: str | None = None

class ChatResponse(BaseModel):
    conversation_id: str
    response: str


conversations: Dict[str, List[Dict[str, str]]] = {}





#this is the chat service
@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # create new conversation if needed

    if request.conversation_id is None:
        conversation_id = str(uuid.uuid4())
        conversations[conversation_id] =[]
    else:
        conversation_id = request.conversation_id
        conversations.setdefault(conversation_id, [])

    # save user message

    conversations[conversation_id].append( {
        "role": "user",
        "content": request.message
    })

    # fake ai response
    ai_response = f"(AI) I received: {request.message}"

    #save AI response
    conversations[conversation_id].append({
         "role": "assistant",
        "content": ai_response
    })

    return {
        "conversation_id": conversation_id,
        "response": ai_response
    }
@app.get("/conversations/{conversation_id}")
def get_conversation(conversation_id: str):
    return {
        "conversation_id": conversation_id,
        "messages": conversations.get(conversation_id, [])
    }
    


