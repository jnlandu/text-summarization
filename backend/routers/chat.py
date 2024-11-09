from fastapi import APIRouter
from fastapi import HTTPException
from utils.api import Client, ChatRequest
from utils.deps import db_dependency, user_dependency


router = APIRouter(
    prefix='/chat',
    tags=['Summarize or Chat']
)

# Dummy list to hold chat messages
chat_history = []
# @router.get('/')
# async def get_chat():
#     return {"messages": chat_history}

@router.post('/')
async def chat(
      db: db_dependency, user: user_dependency, 
      chat_request: ChatRequest,
    #   file: UploadFile = File(...),
     
):
    #  Test chat request:
    try:
        # if   chat_request.content:
            stream = Client.chat.completions.create(
                 messages=[
                    {
                        "role": "system",
                        "content": "You are a wise  assistant. Your name is Okapi. You are helping a user with a question.",
                    },
                    {
                        "role": "user",
                        "content": chat_request.content,
                    },
                ],
                temperature=0.1,
                max_tokens=8192,
                top_p=1,
                stop= None,
                # model="mixtral-8x7b-32768",
                model="llama3-8b-8192",
            )
            for chunk in stream.choices:
                if chunk.message.role == "assistant":
                    response_message = chunk.message.content
                    chat_history.append(chat_request.content) 
                    return {"response": response_message}
            # response_message = stream.choices[0].message.content
            # chat_history.append(chat_request.content)  # Store user message
            # chat_history.append(response_message)  # Store AI response
            # return {"response": response_message}
   
   
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Groq API error: {str(e)}")