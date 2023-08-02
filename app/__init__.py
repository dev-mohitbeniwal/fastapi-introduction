from fastapi import FastAPI, Depends  # add Depends
from fastapi.middleware.cors import CORSMiddleware  # import CORSMiddleware
from sqlmodel import SQLModel
from .database import engine
from .routers import items
from . import models, database

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],  # Allows CORS from this origin
    allow_credentials=True,  # Allows cookies to be sent with requests from the origin
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(items.router)

@app.on_event("startup")
async def startup_event():
    SQLModel.metadata.create_all(engine)
