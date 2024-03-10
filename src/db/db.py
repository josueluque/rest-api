# Importación del módulo necesario para la conexión con MySQL
from sqlalchemy import create_engine, MetaData
from decouple import config

# Establecimiento de la conexión con MySQL
engine = create_engine(config('DATABASE_URL'))
meta = MetaData()
conn = engine.connect().execution_options(isolation_level="AUTOCOMMIT")