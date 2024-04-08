# # Importación del módulo necesario para la conexión con MySQL
# from sqlalchemy import create_engine, MetaData
# from src.config.settings import get_settings

# # Establecimiento de la conexión con MySQL
# settings = get_settings()

# engine = create_engine(settings.DATABASE_URI)
# meta = MetaData()
# conn = engine.connect().execution_options(isolation_level="AUTOCOMMIT")

'''new db connection'''

from src.config.settings import get_settings
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Generator
from sqlalchemy import create_engine

settings = get_settings()

engine = create_engine(settings.DATABASE_URI,
                       pool_pre_ping=True,
                       pool_recycle=3600,
                       pool_size=20,
                       max_overflow=0)

SessionLocal = sessionmaker(bind=engine, autocommit=True, autoflush=False)
Base = declarative_base()


def get_session() -> Generator:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()