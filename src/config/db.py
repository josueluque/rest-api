# Importación del módulo necesario para la conexión con MySQL
from sqlalchemy import create_engine, MetaData
from src.config.settings import get_settings

# Establecimiento de la conexión con MySQL
settings = get_settings()

engine = create_engine(settings.DATABASE_URI)
meta = MetaData()
conn = engine.connect().execution_options(isolation_level="AUTOCOMMIT")