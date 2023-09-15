from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean

from .base import Base


class User(Base):
    email: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(32), nullable=False)
    username: Mapped[str | None] = mapped_column(String(32), unique=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    # profile
    # posts
    # comments
    # cart
