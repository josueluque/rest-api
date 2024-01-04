from fastapi import APIRouter
from src.schemas.userSchema import User
from src.services import userService


user = APIRouter()

#TODO Agregar Exceptions y Status code
#TODO Seperar funciones en user service y agregar docstrings

@user.get("/users")
def get_users():
    return userService.all_users()

@user.post("/user")
def create_user(user: User):
    return userService.new_user(user)

@user.get("/users/{id}")
def get_user(id: str):
    return userService.find_by_id(id)

@user.put("/users/{id}")
def update_user(user: User, id: str):
    return "user edited"

@user.delete("/users/{id}")
def delete_user(id: str):
    return "user deleted"
