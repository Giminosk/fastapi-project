import pytest
import pytest_asyncio
import asyncio
from httpx import AsyncClient
from typing import Generator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from src.models.base import Base
from src.api.users.schemas import UserCreateSchema
from src.api.profiles.schemas import ProfileCreateSchema
from src.app import app
from src.config import settings


async_engine = create_async_engine(
    url=settings.DB_URL,
    echo=True,
    future=True,
)


@pytest.fixture(scope="session", autouse=True)
async def async_session() -> AsyncSession:
    session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

    async with session() as s:
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

        yield s

        # async with async_engine.begin() as conn:
        #     await conn.run_sync(Base.metadata.drop_all)

    # await async_engine.dispose()


@pytest.fixture(scope="session")
def event_loop(request) -> Generator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def async_client():
    async with AsyncClient(app=app, base_url="http://0.0.0.0:8000") as client:
        yield client

    await async_engine.dispose()


@pytest.fixture
def users():
    users = [
        UserCreateSchema(email="user1@example.com", password="123456789"),
        UserCreateSchema(email="user2@example.com", password="123456789"),
        UserCreateSchema(email="user3@example.com", password="123456789"),
    ]
    return users


@pytest.fixture
def profiles():
    profiles = [
        ProfileCreateSchema(first_name="fn1", last_name="ln1", user_id=1),
        ProfileCreateSchema(first_name="fn2", last_name="ln2", user_id=2),
        ProfileCreateSchema(first_name="fn3", last_name="ln3", user_id=3),
    ]
    return profiles
