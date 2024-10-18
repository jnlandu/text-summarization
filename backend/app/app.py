import os 

from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware
from  utils.database import Base, engine
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.middleware("http")
async def add_csp_header(request, call_next):
    response = await call_next(request)
    # Adding Content-Security-Policy to block or upgrade mixed content
    response.headers["Content-Security-Policy"] = "default-src 'self'; upgrade-insecure-requests; block-all-mixed-content"
    return response


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
