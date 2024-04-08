import os 

# Se definen las variables de entorno
env_variables = {
    '# Environment variables'
    '\n''\n'
    '# MySQL Database'
    '\n'
    'MYSQL_HOST': 'localhost',
    'MYSQL_USER': 'root',
    'MYSQL_PASSWORD': 'mysql',
    'MYSQL_PORT': '3306',
    'MYSQL_DB': 'restapidb',
    '\n'
    '# JWT and Secret key'
    '\n'
    'JWT_SECRET':'"secret"',
    'JWT_ALGORITHM':'"HS256"',
    'SECRET_KEY':'"secret_key"',
    '\n'
    '# User Admin'
    '\n'
    'ADMIN_EMAIL':'"admin@gmail.com"',
    'ADMIN_PASSWORD':'"admin"',

}

# Se convierte las variables de entorno en contenido de archivo .env
env_content = "\n".join([f"{key}={value}" for key, value in env_variables.items()])

# Se obtiene la ruta de la carpeta actual
current_directory = os.getcwd()

env_file_name = ".env"

# Se une la ruta de la carpeta actual con el nombre del archivo
env_file_path = os.path.join(current_directory, env_file_name)

# Se escribe el contenido en el archivo .env
try:
    with open(env_file_path, "w") as env_file:
        env_file.write(env_content)
    print(f"Archivo {env_file_path} generado con éxito.")
except IOError as e:
    print(f"Error al escribir en el archivo {env_file_path}: {e}")