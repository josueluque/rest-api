from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:@localhost:3306/restapidb") # Es un objeto de sqlalchemy.create_engine que se utiliza para conectarse a una base de datos

meta = MetaData() # Es un objeto de sqlalchemy.MetaData que se utiliza para almacenar información sobre la estructura de la base de datos, como las tablas y sus columnas.

conn = engine.connect() 



