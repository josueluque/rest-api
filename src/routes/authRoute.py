from fastapi import APIRouter
from starlette import status
from fastapi.responses import JSONResponse
from src.schemas.authSchema import UserManager
from src.libs.jwt_manager import createAccessToken
from decouple import config
from typing import Union

auth = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@auth.post("/login", response_model=Union[str, list])
def login(user: UserManager):
    if user.email == config("ADMIN_EMAIL") and user.password == config("ADMIN_PASSWORD"):
        token: str = createAccessToken(user.__dict__)
        return JSONResponse(status_code = status.HTTP_200_OK, content=token)
    return JSONResponse(content=["El correo o el usuario no son correctos"], status_code = status.HTTP_404_NOT_FOUND)
