from fastapi import APIRouter, status, HTTPException
from src.schemas.userSchema import User
from src.services import userService
from typing import Union


user = APIRouter()


@user.get("/user/users", response_model=list[User], tags=["user"])
def get_users():
    try:
        return userService.all_users()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to get all users. ERROR: {str(e)}")
    

@user.post("/user/createUser", response_model=User, tags=["user"])
def create_user(user: User):
    existing_user = userService.find_by_user_name(user.name)
    if (existing_user):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User could not be created. Existing user: {user.name}")

    try:
        return userService.add_new_user(user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to create user. ERROR: {str(e)}")


@user.get("/user/getUser/{userId}", response_model=Union[User, str], tags=["user"])
def get_user(userId: str):
    existing_user = userService.find_by_user_id(userId)
    if (not existing_user):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User not found, ID: {userId}")

    return existing_user


@user.put("/user/editUser/{userId}", response_model=Union[User, str], tags=["user"])
def update_user(userId: str, user: User):
    existing_user = userService.find_by_user_id(userId)
    if (not existing_user):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User not found, ID: {userId}")
    
    existing_name = userService.find_by_user_name(user.name)
    if (existing_name):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User could not be created. Existing user: {user.name}")

    try:
        return userService.update_by_id(userId, user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to update user, ID: {userId}. ERROR: {str(e)}")


@user.delete("/user/removeUser/{userId}", response_model=str, tags=["user"])
def delete_user(userId: str):
    existing_user = userService.find_by_user_id(userId)
    if (not existing_user):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User not found, ID: {userId}")
    
    try:    
        userService.delete_by_id(userId)
        return f"Successfully deleted, user ID: {userId}"
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to delete user, ID: {userId}. ERROR: {str(e)}")

