from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.sql import func

from datetime import datetime
from .base import Base

from typing import TYPE_CHECKING

# if TYPE_CHECKING:
from .profile import Profile


class User(Base):
    email: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(32), nullable=False)
    username: Mapped[str | None] = mapped_column(String(32), unique=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now()
    )

    profile: Mapped[Profile] = relationship(back_populates="user")

    # posts
    # comments
    # cart
