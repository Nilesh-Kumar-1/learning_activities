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
    prefix="/users",
    tags=["users"]
)

user_dependency = Annotated[dict, Depends(get_current_user)] # Dependency injection to get the current authenticated user
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Userverification(BaseModel):
    password : str
    new_password : str

@router.get("/get_users", status_code=status.HTTP_200_OK)
async def get_users(user: user_dependency, db: db_dependency):
    if user is None or user.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin privileges required")
    return db.query(Users).filter(Users.id == user.id).first()

@router.put("/update_password/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_user(user_verification: Userverification, user: user_dependency, db: db_dependency, user_id: int = Path(gt=0), password: str = None):
    user_model = db.query(Users).filter(Users.id == user_id).first()

    if user is None or user.role != "admin" and user.id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin privileges required")
    if user_model is None:
        raise HTTPException(status_code=404, detail="User not found")
    if user_verification.password:
        if not bcrypt_context.verify(user_verification.password, user_model.hashed_password):
            raise HTTPException(status_code=401, detail="Incorrect password")
        user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)
    db.add(user_model)
    db.commit()
    return {"message": "User updated successfully"}