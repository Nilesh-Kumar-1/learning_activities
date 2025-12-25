from fastapi import Depends, HTTPException, status, Path, APIRouter
from pydantic import BaseModel, Field
from typing import Annotated
import models
from sqlalchemy.orm import Session
from database import SessionLocal
from .auth import get_current_user


router = APIRouter(
    tags=["todos"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)] # # Dependency injection to get a database session using Depends
user_dependency = Annotated[dict, Depends(get_current_user)] # Dependency injection to get the current authenticated user

class TodoItem(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=250)
    priority: int = Field(gt=0, lt=6)
    complete: bool = False

@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(user:user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    return db.query(models.Todos).filter(models.Todos.owner_id == user.id).all()

@router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).filter(models.Todos.owner_id == user.id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo_model

@router.post("/todo/", status_code=status.HTTP_201_CREATED)
async def create_todo(user: user_dependency, todo_item: TodoItem, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    todo_model = models.Todos(
        **todo_item.model_dump(),
        owner_id=user.id
    )
    db.add(todo_model)
    db.commit()
    return todo_model.id

@router.put("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def update_todo(
    db: db_dependency,
    todo_id: int = Path(gt=0),
    todo_item: TodoItem = None, # type: ignore
    user: user_dependency = None
):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).filter(models.Todos.owner_id == user.id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todo_model.title = todo_item.title # type: ignore
    todo_model.description = todo_item.description # type: ignore
    todo_model.priority = todo_item.priority # type: ignore
    todo_model.complete = todo_item.complete # type: ignore

    db.add(todo_model)
    db.commit()
    return {"message": "Todo updated successfully"}

@router.delete("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).filter(models.Todos.owner_id == user.id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo_model)
    db.commit()
    return {"message": "Todo deleted successfully"}