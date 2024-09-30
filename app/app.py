from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

# For cross plateform: We will use the CORSMiddleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)