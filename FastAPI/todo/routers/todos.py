from fastapi import Depends, HTTPException, status, Path, APIRouter
from pydantic import BaseModel, Field
from typing import Annotated
import models
from sqlalchemy.orm import Session
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)] # # Dependency injection to get a database session using Depends

class TodoItem(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=250)
    priority: int = Field(gt=0, lt=6)
    complete: bool = False

@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(models.Todos).all()

@router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo_model

@router.post("/todo/", status_code=status.HTTP_201_CREATED)
async def create_todo(todo_item: TodoItem, db: db_dependency):
    todo_model = models.Todos(
        **todo_item.model_dump()
    )
    db.add(todo_model)
    db.commit()
    return todo_model.id

@router.put("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def update_todo(
    db: db_dependency,
    todo_id: int = Path(gt=0),
    todo_item: TodoItem = None
):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todo_model.title = todo_item.title
    todo_model.description = todo_item.description
    todo_model.priority = todo_item.priority
    todo_model.complete = todo_item.complete

    db.add(todo_model)
    db.commit()
    return {"message": "Todo updated successfully"}

@router.delete("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo_model)
    db.commit()
    return {"message": "Todo deleted successfully"}