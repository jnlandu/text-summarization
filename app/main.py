from fastapi import Depends, HTTPException, status, UploadFile, File
from fastapi.security import  OAuth2PasswordRequestForm

from typing import Annotated

from app.app import app
from utils.auth import authenticate_user, oauth2_scheme
from utils.pdf import extract_text_from_pdf
from utils.summarizer import summarizer

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


@app.post("/summarize/")
async def upload_file(
      form_data: Annotated[OAuth2PasswordRequestForm, Depends(oauth2_scheme)], file: UploadFile = File(...)
):
    

    if file.content_type == "application/pdf":
        content = await extract_text_from_pdf(file)
    elif file.content_type == "text/plain":
        content = await file.read()
        content = content.decode("utf-8")
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    summary = summarizer(content, max_length=100, min_length=30, do_sample=False)
    return {"summary": summary[0]['summary_text']}

print("Server is running correctly")

