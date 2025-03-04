from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Any, Generator
from groq.client import Client
import uuid

router = APIRouter()

class ChatRequest(BaseModel):
    session_id: str
    content: str

# In-memory store for session data
sessions = {}

async def db_dependency():
    # Database dependency logic here
    pass

async def user_dependency():
    # User authentication and validation logic here
    pass

def get_or_create_session(session_id: str):
    if session_id not in sessions:
        sessions[session_id] = []
    return sessions[session_id]

@router.post('/')
async def chat(
    db: Any = Depends(db_dependency),
    user: Any = Depends(user_dependency),
    chat_request: ChatRequest
) -> Generator[dict, None, None]:
    # Retrieve or create a session
    session_history = get_or_create_session(chat_request.session_id)
    
    # Append user's message to history
    session_history.append({"role": "user", "content": chat_request.content})
    
    try:
        stream = Client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a wise assistant. Your name is Okapi. You are helping a user with a question. \
                    You will answer the user in the best way possible. You will be polite and respectful. \
                    You will use the language of the user, that is if it is English, you will use English, if it is French, you will use French."
                },
                *session_history
            ],
            temperature=0.1,
            max_tokens=8192,
            stream=True,
            top_p=1,
            stop=None,
            model="llama3-8b-8192",
        )
        for chunk in stream:
            response_message = chunk.choices[0].delta.content
            if response_message:
                # Append AI's response to history
                session_history.append({"role": "assistant", "content": response_message})
                yield {"response": response_message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
