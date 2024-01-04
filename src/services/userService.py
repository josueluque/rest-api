from src.db.db import conn
from src.models.userModel import users
from cryptography.fernet import Fernet


key = Fernet.generate_key()
f = Fernet(key)

def all_users():
    return conn.execute(users.select()).fetchall()

def new_user(user):
    new_user = {"name": user.name, "email": user.email, "estado": user.estado}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))

    result = conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()

def find_by_id(id):
    return conn.execute(users.select().where(users.c.id == id)).first()
