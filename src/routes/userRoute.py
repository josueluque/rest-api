from fastapi import APIRouter
from src.db.db import conn
from src.models.userModel import users
from src.schemas.userSchema import User
from cryptography.fernet import Fernet


user = APIRouter()

key = Fernet.generate_key()
f = Fernet(key)


@user.get("/users")
def get_users():
    return conn.execute(users.select()).fetchall()

@user.post("/user")
def create_user(user: User):
    new_user = {"name": user.name, "email": user.email}
    new_user["password"] = bytes.decode(f.encrypt(user.password.encode("utf-8")))
    #print(new_user)

    result = conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()
