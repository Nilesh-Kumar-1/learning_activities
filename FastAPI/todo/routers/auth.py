from datetime import timedelta, datetime, timezone
from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from pydantic import BaseModel
from models import Users
from passlib.context import CryptContext
from helpers.common_helper import db_dependency
from jose import jwt, JWTError

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


SECERT_KEY = "9f3a7c2e5d8b41f0c6e2d7a9b4f83c1d7a2e9b6c4f5d8a7e3c1f9d2b6a4e7c8f"
ALGORITHMS = "HS256"
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

class CreateUserRequest(BaseModel):
    username: str
    password: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str

class Token(BaseModel):
    access_token : str
    token_type : str

def authenticate_user(username: str, password: str, db: db_dependency):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password): # type: ignore
        return False
    return user

def create_access_token(username: str, user_id: int, role: str, expires_delta: timedelta = None): # type: ignore

    to_encode = {'sub': username, 'id': user_id, 'role': role}
    expire = datetime.now(timezone.utc) + expires_delta if expires_delta else None
    to_encode.update({'exp': expire})

    return jwt.encode(to_encode, SECERT_KEY, algorithm=ALGORITHMS)

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)], db: db_dependency):
    try:
        payload = jwt.decode(token, SECERT_KEY, algorithms=[ALGORITHMS])
        username = payload.get("sub")
        user_id = payload.get("id")
        user_role = payload.get("role")
        if username is None or user_id is None:
            return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
        token_data = username
    except JWTError as e:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
    user = db.query(Users).filter(Users.username == token_data).first()
    return user

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db:db_dependency, user_request: CreateUserRequest):
    create_user = Users(
        username=user_request.username,
        email=user_request.email,
        first_name=user_request.first_name,
        last_name=user_request.last_name,
        hashed_password=bcrypt_context.hash(user_request.password),
        role=user_request.role,
        is_active=True
    )
    db.add(create_user)
    db.commit()
    return {"message": f"{create_user.username} created successfully"}

@router.post("/token", status_code=status.HTTP_200_OK, response_model=Token)
async def login_for_access_token(db: db_dependency, form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
    token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20)) # type: ignore
    return {"access_token": f"{token}", "token_type": "bearer"}
