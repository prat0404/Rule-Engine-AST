from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "YOUR_DB_LINK" #sqlite+aiosqlite:///./rules.db


settings = Settings()
