from functools import lru_cache
from pydantic_settings import BaseSettings
from decouple import config


class Settings(BaseSettings):

    # App
    APP_NAME:  str = config("APP_NAME", "App FastAPI")
    DEBUG: bool = bool(config("DEBUG", False))
    
    # FrontEnd Application
    FRONTEND_HOST: str = config("FRONTEND_HOST", "http://localhost:5173")

    # MySql Database Config
    MYSQL_HOST: str = config("MYSQL_HOST", 'localhost')
    MYSQL_USER: str = config("MYSQL_USER", 'root')
    MYSQL_PASS: str = config("MYSQL_PASSWORD", '')
    MYSQL_PORT: int = int(config("MYSQL_PORT", 3306))
    MYSQL_DB: str = config("MYSQL_DB", 'fastapi')
    # DATABASE_URI: str = f"mysql+pymysql://{MYSQL_USER}:%s@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}" % quote_plus(MYSQL_PASS)
    DATABASE_URI: str = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

    # JWT Secret Key
    JWT_SECRET: str = config("JWT_SECRET", "")
    JWT_ALGORITHM: str = config("ACCESS_TOKEN_ALGORITHM", "HS256")
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = int(config("ACCESS_TOKEN_EXPIRE_MINUTES", 3))
    # REFRESH_TOKEN_EXPIRE_MINUTES: int = int(config("REFRESH_TOKEN_EXPIRE_MINUTES", 1440))

    # App Secret Key
    SECRET_KEY: str = config("SECRET_KEY", "")


@lru_cache()
def get_settings() -> Settings:
    return Settings()