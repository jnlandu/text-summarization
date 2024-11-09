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
                        "content": "You are a wise  assistant. Your name is Okapi. You are helping a user with a question.\
                        You will answer the user in the best way possible. You will be polite and respectful.\
                        You will use the language of the user, that is if it is English, you will use English, if it is French, you will use French.",
                    },
                    {
                        "role": "user",
                        "content": chat_request.content,
                    },
                ],
                temperature=0.1,
                max_tokens=8192,
                stream=True,
                top_p=1,
                stop= None,
                model="llama3-8b-8192",
            )
            for chunk in stream:
                response_message = chunk.choices[0].delta.content
                if response_message:
                     yield {"response": response_message}

                # if chunk.message.role == "assistant":
                #     response_message = chunk.message.content
                #     chat_history.append(chat_request.content) 
                #     return {"response": response_message}
            # response_message = stream.choices[0].message.content
            # chat_history.append(chat_request.content)  # Store user message
            # chat_history.append(response_message)  # Store AI response
            # return {"response": response_message}
   
   
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Groq API error: {str(e)}")