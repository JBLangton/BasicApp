# app / main.py
from fastapi import FastAPI
from backend.app.database import engine, Base
# Ensure the User model is imported before table creation
from backend.app.controllers import user_controller
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_controller.router, prefix="/users", tags=["users"])

origins = [
    "http://localhost:5173",  # Assuming your frontend runs on port 3000
    # Add other origins (frontend deployments, etc.) if necessary
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
