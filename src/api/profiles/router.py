from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import (
    ProfileCreateSchema,
    ProfileUpdateSchema,
    ProfileGetSchema,
    ProfileUpdatePartialSchema,
)
from . import crud
from src.db_manager import db_manager
from .dependencies import profile_by_id
from src.models.profile import Profile


router = APIRouter(tags=["profiles"])


@router.get("/", response_model=list[ProfileGetSchema])
async def get_all_profiles(
    session: AsyncSession = Depends(db_manager.get_async_session),
):
    return await crud.get_all_profiles(session=session)


@router.get("/{id}", response_model=ProfileGetSchema)
async def get_profile_by_id(
    profile: ProfileCreateSchema = Depends(profile_by_id),
):
    return profile


@router.get("/by_user_id/{user_id}", response_model=ProfileGetSchema)
async def get_profile_by_user_id(
    user_id: int,
    session: AsyncSession = Depends(db_manager.get_async_session),
):
    return await crud.get_profile_by_user_id(session=session, user_id=user_id)


@router.post("/", response_model=ProfileGetSchema, status_code=status.HTTP_201_CREATED)
async def create_profile(
    profile: ProfileCreateSchema,
    session: AsyncSession = Depends(db_manager.get_async_session),
):
    return await crud.create_profile(session=session, profile_in=profile)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_profile(
    profile: Profile = Depends(profile_by_id),
    session: AsyncSession = Depends(db_manager.get_async_session),
) -> None:
    await crud.delete_profile(session=session, profile=profile)


@router.put("/{id}", response_model=ProfileGetSchema, status_code=status.HTTP_200_OK)
async def update_profile(
    profile_in: ProfileUpdateSchema,
    profile: Profile = Depends(profile_by_id),
    session: AsyncSession = Depends(db_manager.get_async_session),
):
    return await crud.update_profile(
        session=session, profile=profile, profile_in=profile_in, partial=False
    )


@router.patch("/{id}", response_model=ProfileGetSchema, status_code=status.HTTP_200_OK)
async def partial_update_profile(
    profile_in: ProfileUpdatePartialSchema,
    profile: Profile = Depends(profile_by_id),
    session: AsyncSession = Depends(db_manager.get_async_session),
):
    return await crud.update_profile(
        session=session, profile=profile, profile_in=profile_in, partial=True
    )
