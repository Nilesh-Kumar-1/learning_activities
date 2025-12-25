from datetime import timedelta, datetime, timezone
from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends, Path
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from pydantic import BaseModel
from models import Users
from passlib.context import CryptContext
from helpers.common_helper import db_dependency
from jose import jwt, JWTError
from .auth import get_current_user

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

user_dependency = Annotated[dict, Depends(get_current_user)] # Dependency injection to get the current authenticated user

@router.get("/only-admin", status_code=status.HTTP_200_OK)
def admin_only(user: user_dependency, db: db_dependency):
    if user is None or user.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin privileges required")
    return db.query(Users).all()

@router.delete("/user/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user: user_dependency, db: db_dependency, user_id: int = Path(gt=0)):
    if user is None or user.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin privileges required")
    user_model = db.query(Users).filter(Users.id == user_id).first()
    if user_model is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user_model)
    db.commit()
    return {"message": "User deleted successfully"}