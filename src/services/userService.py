from src.db.db import conn
from src.models.userModel import users
from cryptography.fernet import Fernet
from sqlalchemy.exc import SQLAlchemyError

import re


key = Fernet.generate_key()
f = Fernet(key)

def all_users():
    """Retrieves all users from the database.

    Returns:
        list of dict: A list of dictionaries with all users. Each dictionary contains information about one user

    Raises:
        ValueError: If there is a problem with the execution of the query.
    """
    try:
        query = users.select()
        return conn.execute(query).fetchall()
    except SQLAlchemyError as e:
        raise ValueError(e)


def add_new_user(user):
    """Given the user object with the entered data. Adds a new user to the database.

    Args:
        user (User): An object User representing the new user.

    Returns:
        dict: A dictionary with the newly created user.

    Raises:
        ValueError: If there is an issue with the execution of the query or an error is encountered during validation.
    """
    try:
        valid_email = validate_email(user.email)
        if (not valid_email):
            raise TypeError("Invalid email format")

        encrypt_password = f.encrypt(user.password.encode("utf-8"))
        new_user = {"name": user.name, "email": user.email, "password": encrypt_password, "state": user.state}

        query = users.insert().values(new_user)
        result = conn.execute(query)

        return find_by_user_id(id = result.lastrowid)
    except SQLAlchemyError as e:
        raise ValueError(e)


def update_by_id(id, user):
    """Updates user information based on the provided user ID and the user object with the entered data.

    Args:
        id (int): The unique identifier of the user to be updated.
        user (User): An object User representing the updated user information.

    Raises:
        ValueError: If there is an issue with the execution of the query or an error is encountered during validation.

    Returns:
        dict: A dictionary with the updated user information.
    """
    try:
        valid_email = validate_email(user.email)
        if (not valid_email):
            raise TypeError("Invalid email format")
        
        encrypt_password  = f.encrypt(user.password.encode("utf-8"))
        query = users.update().values(name = user.name, email = user.email, password = encrypt_password).where(users.c.id == id)
        conn.execute(query)

        return find_by_user_id(id)
    except SQLAlchemyError as e:
        raise ValueError(e)


def delete_by_id(id):
    """Deletes a user from the database based on the provided user ID.

    Args:
        id (int): The unique identifier of the user to be deleted.

    Raises:
        ValueError: If there is an issue with the execution of the query.   
    """
    try:
        query = users.delete().where(users.c.id == id)
        conn.execute(query)
    except SQLAlchemyError as e:
        raise ValueError(e)


def find_by_user_id(id):
    """Finds and retrieves a user from the database based on the provided user ID.

    Args:
        id (int): The unique identifier of the user to be retrieved.

    Returns:
        Object Row or None: A row containing user information if the user is found, or None if the user is not found.
    """
    query = users.select().where(users.c.id == id)
    return conn.execute(query).first()


def find_by_user_name(name):
    """Finds and retrieves a user from the database based on the provided username.

    Args:
        name (str): The username of the user to be retrieved.

    Returns:
        Object Row or None: A row containing user information if the user is found, or None if the user is not found.
    """
    query = users.select().where(users.c.name == name)
    return conn.execute(query).first()


def validate_email(email):
    """Validates an email address.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    if not isinstance(email, str) or not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$", email):
        return False
    return True    