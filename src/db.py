from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from config import settings


class DBManager:
    def __init__(self, db_url: str, db_echo: bool = False):

        self.engine = create_async_engine(
            db_url,
            echo=db_echo,
        )


db_manager = DBManager(
    db_url=settings.DB_URL,
    db_echo=settings.DB_ECHO,
)
