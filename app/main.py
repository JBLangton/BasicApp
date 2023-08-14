# app / main.py
import logging
from fastapi import FastAPI
from app.database import engine, Base
# Ensure the User model is imported before table creation
from app.models.user import User
from app.controllers import user_controller

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_controller.router, prefix="/users", tags=["users"])

