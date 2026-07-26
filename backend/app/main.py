import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Load .env before anything else
load_dotenv()

from app.api.routes import router

app = FastAPI(title="NLP Agent Backend")

# CORS — allow the React frontend (any origin for flexibility)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def health():
    return {"status": "ok"}
