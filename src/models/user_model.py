# from sqlalchemy import Table, Column
# from sqlalchemy.sql.sqltypes import Integer, String, Boolean
# from src.config.db import meta, engine

# users = Table("users", meta, 
#             Column("id", Integer(), primary_key=True), 
#             Column("name", String(50)),
#             Column("email", String(70)),
#             Column("password", String(125)),
#             Column("state", Boolean(), default=False))

# meta.create_all(engine) # Creará todas las tablas definidas en el objeto meta en la base de datos especificada por el objeto engine.

'''new model user'''

from sqlalchemy import Boolean, Column, DateTime, Integer, String, func
from src.config.db import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150))
    email = Column(String(255), unique=True, index=True)
    password = Column(String(100))
    is_active = Column(Boolean, default=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())