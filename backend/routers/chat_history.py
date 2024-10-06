from fastapi import APIRouter
from fastapi import HTTPException
from utils.api import Client, ChatRequest
from utils.deps import db_dependency, user_dependency


router = APIRouter(
    prefix='/chat',
    tags=['Summarize or Chat']
)

# Dummy list to hold chat messages

    