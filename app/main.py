from fastapi import Depends, HTTPException, status, UploadFile, File
from fastapi.security import  OAuth2PasswordRequestForm

from typing import Annotated

from app.app import app
from utils.api import Client, ChatRequest
from utils.auth import authenticate_user, oauth2_scheme
from utils.pdf import extract_text_from_pdf
# from utils.summarizer import summarizer

@app.get("/")
async def root():
    return {"message": "Healthy"}

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"Authenticated_user": user["username"], "Password": user["password"]}


@app.post("/chat")
async def chat(
      form_data: Annotated[OAuth2PasswordRequestForm, Depends(oauth2_scheme)], 
      chat_request: ChatRequest,
    #   file: UploadFile = File(...),
     
):
    #  Test chat request:
    try:
        # if   chat_request.content:
            chat_completion = Client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": chat_request.content,
                    }
                ],
                model="llama3-8b-8192",
            )
            response_message = chat_completion.choices[0].message.content
            return {"response": response_message}

    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Groq API error: {str(e)}")
    
print("Server is running correctly")


