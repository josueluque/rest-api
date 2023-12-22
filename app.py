from fastapi import FastAPI
from src.routes.userRoute import user

app = FastAPI()

app.include_router(user)
