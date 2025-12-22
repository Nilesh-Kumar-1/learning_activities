from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from models import Users

router = APIRouter()

class CreateUserRequest(BaseModel):
    username: str
    password: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str

@router.post("/auth/")
async def create_user(user_request: CreateUserRequest):
    create_user = Users(
        username=user_request.username,
        email=user_request.email,
        first_name=user_request.first_name,
        last_name=user_request.last_name,
        hashed_password=user_request.password,
        role=user_request.role,
        is_active=True
    )
    return {"message": "Login endpoint"}