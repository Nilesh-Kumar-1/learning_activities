from fastapi import FastAPI
from router import chat, similarity, storage_account

app = FastAPI(
    title="My Gen AI Learning Application",
    description="This is a sample FastAPI application demonstrating integrating Open AI models with FastAPI.",
    version="1.0.0"
)

app.include_router(chat.router)
app.include_router(similarity.router)
app.include_router(storage_account.router)

