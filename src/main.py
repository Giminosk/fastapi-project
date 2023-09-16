from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from fastapi_users import fastapi_users, FastAPIUsers

from api.users.auth import auth_backend
from api.users.user_manager import get_user_manager
from api.users.schemas import UserRead, UserCreate, UserUpdate

from db import db_manager
from models.base import Base
from models.user import User

from api import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_manager.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(debug=True, lifespan=lifespan)
app.include_router(api_router, prefix="/api")

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


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
