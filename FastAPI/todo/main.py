from fastapi import FastAPI
import models
from routers import auth, todos
from database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine) # Create the database tables if they don't exist mentioned in models.py using the engine from database.py

app.include_router(auth.router) # Include the auth router from models.py for authentication endpoints
app.include_router(todos.router) # Include the auth router from models.py for authentication endpoints