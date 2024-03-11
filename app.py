from fastapi import FastAPI
from src.routes.userRoute import user
from src.routes.authRoute import auth
from src.middlewares.errorHandler import ErrorHandler
import uvicorn

# Creación de la aplicación FastAPI
app = FastAPI(
    title="System Users API",
    description="REST API using Python, FastAPI, MySQL and SQLAlchemy ",
    version="0.1.0"
)

# Incorporando middlewares
app.add_middleware(ErrorHandler)

# Inclusión de rutas adicionales desde el conjunto de rutas 'user'
app.include_router(user)
app.include_router(auth)

# Ejecución del servidor Uvicorn
if __name__ == "__main__":
    uvicorn.run("app:app", port=8000, log_level="info", reload=True)
    