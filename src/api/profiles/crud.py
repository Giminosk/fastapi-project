from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from fastapi import HTTPException, status

from .shemas import ProfileCreateSchema, ProfileUpdateSchema, ProfileUpdatePartialSchema
from src.models.profile import Profile
from src.models.user import User


async def get_profile_by_id(session: AsyncSession, profile_id: int) -> Profile | None:
    return await session.get(Profile, profile_id)


async def get_profile_by_user_id(session: AsyncSession, user_id: int) -> Profile | None:
    query = select(Profile).where(Profile.user_id == user_id)
    profile: Profile | None = await session.scalar(query)
    return profile


async def get_all_profiles(session: AsyncSession) -> list[Profile]:
    query = select(Profile).order_by(Profile.id)
    result: Result = await session.execute(query)
    profiles = result.scalars().all()
    return list(profiles)


async def create_profile(
    session: AsyncSession, profile_in: ProfileCreateSchema
) -> Profile:

    query = select(User).where(User.id == profile_in.user_id)
    result = await session.execute(query)
    if len(list(result.scalars())) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User does not exist",
        )

    query = select(Profile).where(Profile.user_id == profile_in.user_id)
    result = await session.execute(query)
    if len(list(result.scalars())) > 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already has a profile",
        )

    profile: Profile = Profile(**profile_in.model_dump())
    session.add(profile)
    await session.commit()
    return profile


async def delete_profile(session: AsyncSession, profile: Profile) -> None:
    await session.delete(profile)
    await session.commit()


async def update_profile(
    session: AsyncSession,
    profile: Profile,
    profile_in: ProfileUpdateSchema | ProfileUpdatePartialSchema,
    partial: bool = True,
) -> Profile:
    for key, value in profile_in.model_dump(exclude_unset=partial).items():
        setattr(profile, key, value)
    await session.commit()
    return profile
