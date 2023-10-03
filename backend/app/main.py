# app / main.py
from fastapi import FastAPI
from backend.app.database import engine, Base
# Ensure the User model is imported before table creation
from backend.app.controllers import user_controller

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_controller.router, prefix="/users", tags=["users"])

