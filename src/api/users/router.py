from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import UserSchema, UserCreateSchema
from src.db import db_manager


router = APIRouter(tags=["users"])


@router.get("/", response_model=list[UserSchema])
async def get_users(session: AsyncSession = Depends(db_manager.get_async_session)):
    return await crud.get_users(session=session)


@router.post("/", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_in: UserCreateSchema,
    session: AsyncSession = Depends(db_manager.get_async_session),
):
    return await crud.create_user(session=session, user_in=user_in)
