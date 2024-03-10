from jwt import encode, decode
from decouple import config

def createAccessToken(data: dict) -> str:
    token: str = encode(payload=data, key=config('SECRET_KEY'), algorithm='HS256')
    return token


def validateToken(token: str) -> dict:
    data: dict = decode(token, key=config('SECRET_KEY'), algorithms=["HS256"])
    return data


