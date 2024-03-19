from pydantic import BaseModel

class UserManager(BaseModel):
    email:str
    password:str

