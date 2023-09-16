from pydantic import EmailStr
from fastapi_users import schemas
from datetime import datetime


class UserRead(schemas.BaseUser[int]):
    id: int
    email: EmailStr
    username: str
    created_at: datetime
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    password: str
    username: str | None = None
    is_active: bool | None = True
    is_superuser: bool | None = False
    is_verified: bool | None = False


class UserUpdate(schemas.BaseUserUpdate):
    password: str | None = None
    email: EmailStr | None = None
    username: str | None = None
    is_active: bool | None = None
    is_superuser: bool | None = None
    is_verified: bool | None = None
