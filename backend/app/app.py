import os 

from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware
from  utils.database import Base, engine
from dotenv import load_dotenv

load_dotenv()

# API_URL = os.getenv("API_URL") for development

app = FastAPI()
# For cross plateform: use the CORSMiddleware to allow requests from the frontend

origins = [ "*"
    "https://mlops-project-3repcia0n-jeremies-projects-257f201c.vercel.app", # for production
    "http://localhost:3000", # for local development
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
