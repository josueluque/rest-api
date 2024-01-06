from fastapi import APIRouter, status, HTTPException
from src.schemas.userSchema import User
from src.services import userService
from typing import Union


user = APIRouter()

#TODO Agregar Exceptions y Status code
#TODO Seperar funciones en user service y agregar docstrings

@user.get("/user/users", response_model=list[User], tags=["user"])
def get_users():
    try:
        return userService.all_users()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to get all users. ERROR: {str(e)}")
    
@user.post("/user/createUser", response_model=User, tags=["user"])
def create_user(user: User):
    try:
        return userService.add_new_user(user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to create user. ERROR: {str(e)}")


@user.get("/user/getUser/{userId}", response_model=Union[User, str], tags=["user"])
def get_user(id: str):
    existing_user = userService.find_by_id(id)
    if existing_user:
        return existing_user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User not found, ID: {id}")


@user.put("/user/editUser/{userId}", response_model=Union[User, str], tags=["user"])
def update_user(id: str, user: User):
    existing_user = userService.find_by_id(id)
    if (existing_user):
        try:
            return userService.update_by_id(id, user)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to update user, ID: {id}. ERROR: {str(e)}")

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User not found, ID: {id}")


@user.delete("/user/removeUser/{userId}", response_model=str, tags=["user"])
def delete_user(id: str):
    existing_user = userService.find_by_id(id)
    if (existing_user):
        try:
            userService.delete_by_id(id)
            return f"Successfully deleted, user ID: {id}"
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to delete user, ID: {id}. ERROR: {str(e)}")

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User not found, ID: {id}")
