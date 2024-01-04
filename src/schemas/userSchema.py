from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    password: str
    estado: bool

    # class Config:
    #     orm_mode = True

