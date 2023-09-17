from pydantic import BaseModel
from typing import Annotated
from annotated_types import MinLen, MaxLen
from datetime import date


class ProfileBaseSchema(BaseModel):
    first_name: Annotated[str | None, MaxLen(32)] = None
    last_name: Annotated[str | None, MaxLen(32)] = None
    bio: Annotated[str | None, MinLen(10), MaxLen(1000)] = None
    birthdate: date | None = None


class ProfileGetSchema(ProfileBaseSchema):
    user_id: int


class ProfileUpdateSchema(ProfileBaseSchema):
    first_name: Annotated[str, MaxLen(32)]
    last_name: Annotated[str, MaxLen(32)]
    bio: Annotated[str, MinLen(10), MaxLen(1000)]
    birthdate: date


class ProfileUpdatePartialSchema(ProfileBaseSchema):
    pass


class ProfileCreateSchema(ProfileBaseSchema):
    user_id: int
