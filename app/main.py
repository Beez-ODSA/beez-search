from fastapi import FastAPI
from app.routers import search

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Search service is running"}

app.include_router(search.router)