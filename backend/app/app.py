import os 

from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware
from  utils.database import Base, engine
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")



app = FastAPI()
# For cross plateform: We will use the CORSMiddleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[API_URL ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)