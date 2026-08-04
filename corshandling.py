from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from config import settings

app = FastAPI()

#Allowed Origins for frontend

origins = [
    settings.origins
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application with CORS handling!"}