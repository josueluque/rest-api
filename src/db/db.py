# Importación del módulo necesario para la conexión con MySQL
from sqlalchemy import create_engine, MetaData
from decouple import config

# Establecimiento de la conexión con MySQL
engine = create_engine(config('DATABASE_URL'))

meta = MetaData() # Es un objeto de sqlalchemy.MetaData que se utiliza para almacenar información sobre la estructura de la base de datos, como las tablas y sus columnas.

conn = engine.connect().execution_options(isolation_level="AUTOCOMMIT")
