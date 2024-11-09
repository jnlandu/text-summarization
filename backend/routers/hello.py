from fastapi import APIRouter
from fastapi import HTTPException
from utils.api import Client, ChatRequest
from utils.deps import db_dependency, user_dependency



router = APIRouter(
    prefix='/hello',
    tags=['Hello']
)

@router.get('/')
async def hello(message: str,
        db: db_dependency, user: user_dependency,
                ):
    return {'content': message}
