from pydantic import BaseModel, EmailStr
from typing import Annotated
from annotated_types import MinLen, MaxLen


class UserSchema(BaseModel):
    email: EmailStr
    password: Annotated[str, MinLen(8), MaxLen(100)]
    username: Annotated[str, MinLen(3), MaxLen(32)]
    is_verified: bool
    is_active: bool


class UserCreateSchema(BaseModel):
    email: EmailStr
    password: Annotated[str, MinLen(8), MaxLen(32)]
    username: Annotated[str, MinLen(3), MaxLen(32)]
