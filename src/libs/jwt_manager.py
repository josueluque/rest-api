from jwt import encode, decode
from src.config.settings import get_settings


settings = get_settings()


def createAccessToken(data: dict) -> str:
    token: str = encode(payload=data, key=settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return token


def validateToken(token: str) -> dict:
    data: dict = decode(token, key=settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
    return data


