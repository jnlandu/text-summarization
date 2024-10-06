import os 

from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware
from  utils.database import Base, engine
from dotenv import load_dotenv

load_dotenv()

# API_URL = os.getenv("API_URL") for development



app = FastAPI()
# For cross plateform: We will use the CORSMiddleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://okapi-ia.azurewebsites.net"], # for production put the frontend url
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)