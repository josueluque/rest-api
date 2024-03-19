from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from src.config.db import meta, engine

users = Table("users", meta, 
            Column("id", Integer(), primary_key=True), 
            Column("name", String(50)),
            Column("email", String(70)),
            Column("password", String(125)),
            Column("state", Boolean(), default=False))

meta.create_all(engine) # Creará todas las tablas definidas en el objeto meta en la base de datos especificada por el objeto engine.
