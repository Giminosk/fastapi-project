from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager

from db import db_manager
from models.base import Base

from api import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_manager.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(debug=True, lifespan=lifespan)
app.include_router(api_router, prefix="/api")


@app.get("/")
def hello():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
