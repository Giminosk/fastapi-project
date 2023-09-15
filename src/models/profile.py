from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Date, ForeignKey

from datetime import date
from .base import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User


class Profile(Base):
    first_name: Mapped[str | None] = mapped_column(String(32))
    last_name: Mapped[str | None] = mapped_column(String(32))
    bio: Mapped[str | None] = mapped_column(String(500))
    birthdate: Mapped[date | None] = mapped_column(Date)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="profile")
