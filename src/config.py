from pathlib import Path
from pydantic_settings import BaseSettings

import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    DB_URL: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
    DB_ECHO: bool = True
    RESET_PASSWORD_SECRET: str = os.environ.get("RESET_PASSWORD_SECRET")
    VERIF_SECRET: str = os.environ.get("VERIF_SECRET")
    JWT_SECRET: str = os.environ.get("JWT_SECRET")


settings = Settings()
