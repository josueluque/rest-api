from src.db.db import conn
from src.models.userModel import users
from cryptography.fernet import Fernet


key = Fernet.generate_key()
f = Fernet(key)

def all_users():
    query = users.select()
    return conn.execute(query).fetchall()

def add_new_user(user):
    new_user = {"name": user.name, "email": user.email, "estado": user.estado}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))

    query = users.insert().values(new_user)
    result = conn.execute(query)

    query_rerturn = users.select().where(users.c.id == result.lastrowid)
    return conn.execute(query_rerturn).first()

def find_by_id(id):
    query = users.select().where(users.c.id == id)
    return conn.execute(query).first()

def update_by_id(id, user):
    query = users.update().values(name = user.name, email = user.email, password = f.encrypt(user.password.encode("utf-8"))).where(users.c.id == id)
    conn.execute(query)

    query_return = users.select().where(users.c.id == id)
    return conn.execute(query_return).first()


def delete_by_id(id):
    query = users.delete().where(users.c.id == id)
    return conn.execute(query)

