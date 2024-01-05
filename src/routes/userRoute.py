from fastapi import APIRouter, Response, status
from src.schemas.userSchema import User
from src.services import userService
from starlette.status import HTTP_204_NO_CONTENT


user = APIRouter()

#TODO Agregar Exceptions y Status code
#TODO Seperar funciones en user service y agregar docstrings

@user.get("/user/users", response_model=list[User], tags=["user"])
def get_users():
    return userService.all_users()

@user.post("/user/createUser", response_model=User, tags=["user"])
def create_user(user: User):
    return userService.add_new_user(user)

@user.get("/user/getUser/{userId}", tags=["user"])
def get_user(id: str):
    result = userService.find_by_id(id)
    if (result):
        return result
    else: 
        return f"No se encontro el usuario con id: {id}"

@user.put("/user/editUser/{userId}", response_model=User, tags=["user"])
def update_user(id: str,user: User):
    exis_user = userService.find_by_id(id)
    if (exis_user):
        return userService.update_by_id(id,user)
    else:
        return "Failed to update user"


@user.delete("/user/removeUser/{userId}", tags=["user"])
def delete_user(id: str):
    exis_user = userService.find_by_id(id)
    if (exis_user):
        userService.delete_by_id(id)
        return "Successfully deleted"
    else:
        return "Failed to delete user"
