from fastapi import FastAPI
from src.routes.userRoute import user
import uvicorn

app = FastAPI(
    title="System Users API",
    description="REST API using Python, FastAPI, MySQL and SQLAlchemy ",
    version="0.1.0"
)

app.include_router(user)


if __name__ == "__main__":
    uvicorn.run("app:app", port=8000, log_level="info", reload=True)
    