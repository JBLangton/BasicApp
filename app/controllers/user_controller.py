# app / controllers / user_controller.py
import logging
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.views.user_views import UserBase, User
from app.models.user import User as DBUser
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=User)
def create_user(user: UserBase, db: Session = Depends(get_db)):
    logging.info(f"Attempting to create user with email: {user.email}")

    db_user = DBUser(**user.dict())
    db.add(db_user)

    try:
        db.commit()
        logging.info(f"User with email {user.email} created successfully.")
    except Exception as e:
        logging.error(f"Error while committing user with email {user.email}: {str(e)}")
        db.rollback()

    db.refresh(db_user)
    return db_user
