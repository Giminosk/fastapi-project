from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase

from config import settings
from models.user import User


class DBManager:
    def __init__(self, db_url: str, db_echo: bool = False):

        self.engine = create_async_engine(
            db_url,
            echo=db_echo,
        )

        self.session_maker = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
            autocommit=False,
            autoflush=False,
        )

    async def get_async_session(self) -> AsyncSession:
        async with self.session_maker() as session:
            yield session
            await session.close()


db_manager = DBManager(
    db_url=settings.DB_URL,
    db_echo=settings.DB_ECHO,
)


async def get_user_db(session: AsyncSession = Depends(db_manager.get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
