from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from src.libs.jwt_manager import validateToken
from decouple import config
from starlette import status


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)  # Llama al metodo __call__ de la clase superior HTTPBearer, y me devuelve los datos de las credeciales del usuario
        data = validateToken(auth.credentials)  # Desencripta y devuelve los datos en un diccionario
        print(data)
        if data['email'] != config("ADMIN_EMAIL"):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
