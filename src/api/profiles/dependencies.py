from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

from src.db_manager import db_manager
from src.models import Profile
from . import crud


async def profile_by_id(
    profile_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_manager.get_async_session),
) -> Profile:
    profile = await crud.get_profile_by_id(session=session, profile_id=profile_id)
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Profile {profile_id} not found",
        )
    return profile
