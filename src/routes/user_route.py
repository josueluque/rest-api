from fastapi import APIRouter, HTTPException, Path, Depends
from starlette import status
from fastapi.responses import JSONResponse
from src.schemas.user_schema import User
from src.middlewares.credential_middleware import JWTBearer
from src.services import user_service
from typing import Union


user = APIRouter(
    prefix="/user",
    tags=['user'],
    dependencies=[Depends(JWTBearer())]
)


@user.get("/users", response_model=list[User])
def get_users():
    try:
        return user_service.all_users()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to get all users. ERROR: {str(e)}")
    

@user.post("/createUser", response_model=User)
def create_user(user: User):
    existing_user = user_service.find_by_user_name(user.name)
    if (existing_user):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User could not be created. Existing user: {user.name}")

    try:
        return user_service.add_new_user(user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to create user. ERROR: {str(e)}")


@user.get("/getUser/{userId}", response_model=Union[User, str])
def get_user(userId: int = Path(ge=1, le=2000)):
    existing_user = user_service.find_by_user_id(userId)
    if (not existing_user):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User not found, ID: {userId}")

    return existing_user


@user.put("/editUser/{userId}", response_model=Union[User, str])
def update_user(user: User, userId: int = Path(ge=1, le=2000)):
    existing_user = user_service.find_by_user_id(userId)
    if (not existing_user):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User not found, ID: {userId}")
    
    existing_name = user_service.find_by_user_name(user.name)
    if (existing_name):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User could not be updated. Existing user: {user.name}")

    try:
        return user_service.update_by_id(userId, user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to update user, ID: {userId}. ERROR: {str(e)}")


@user.delete("/removeUser/{userId}", response_model=str)
def delete_user(userId: int = Path(ge=1, le=2000)):
    existing_user = user_service.find_by_user_id(userId)
    if (not existing_user):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User not found, ID: {userId}")
    
    try:    
        user_service.delete_by_id(userId)
        return JSONResponse(content=f"Successfully deleted, user ID: {userId}", status_code=status.HTTP_202_ACCEPTED)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to delete user, ID: {userId}. ERROR: {str(e)}")

