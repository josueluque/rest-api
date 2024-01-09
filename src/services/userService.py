from src.db.db import conn
from src.models.userModel import users
from cryptography.fernet import Fernet
import re

key = Fernet.generate_key()
f = Fernet(key)

def all_users():
    query = users.select()
    return conn.execute(query).fetchall()


def find_by_user_id(id):
    query = users.select().where(users.c.id == id)
    return conn.execute(query).first()


def find_by_user_name(name):
    query = users.select().where(users.c.name == name)
    return conn.execute(query).first()


def validate_email(email):
    if not isinstance(email, str) or not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$", email):
        return False
    return True    

def add_new_user(user):
    valid_email = validate_email(user.email)
    if (not valid_email):
        raise TypeError("Invalid email format")

    encrypt_password = f.encrypt(user.password.encode("utf-8"))
    new_user = {"name": user.name, "email": user.email, "password": encrypt_password, "state": user.state}

    query = users.insert().values(new_user)
    result = conn.execute(query)

    return find_by_user_id(id = result.lastrowid)



def update_by_id(id, user):
    encrypt_password  = f.encrypt(user.password.encode("utf-8"))
    query = users.update().values(name = user.name, email = user.email, password = encrypt_password).where(users.c.id == id)
    conn.execute(query)

    return find_by_user_id(id)


def delete_by_id(id):
    query = users.delete().where(users.c.id == id)
    return conn.execute(query)

