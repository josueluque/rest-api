from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    """
    - Validaciones con Field - 
    -> max_length = cantidad maxima de caracteres (int)
    -> min_lenght = cantidad minima de caracteres (int)
    -> default = mensaje que aparecera en el campo a completar (str)

    name: str = Field(default="My name", min_length=2, max_length=15) 
    """
    id: Optional[int] = None
    name: str = Field(max_length=15)    
    email: EmailStr
    password: str
    state: Optional[bool] = False

    class Config:
        # orm_mode = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Example Name",
                "email": "example@gmail.com",
                "password": "Secure Password",
                "state": False,
            }
        }

