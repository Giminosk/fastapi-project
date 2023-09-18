from pathlib import Path
from pydantic_settings import BaseSettings

import os
from dotenv import load_dotenv

load_dotenv()

# BASE_DIR = Path(__file__).resolve().parent.parent

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")


class Settings(BaseSettings):
    DB_URL: str = "sqlite+aiosqlite:///tests/db_test.sqlite3"
    # DB_URL: str = (
    #     # f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{POSTGRES_DB}"
    #     f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}/{POSTGRES_DB}"
    # )
    DB_ECHO: bool = True

    RESET_PASSWORD_SECRET: str = os.environ.get("RESET_PASSWORD_SECRET")
    VERIF_SECRET: str = os.environ.get("VERIF_SECRET")
    JWT_SECRET: str = os.environ.get("JWT_SECRET")


settings = Settings()
