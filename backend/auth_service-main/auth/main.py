from fastapi import FastAPI
from auth.routes import router as auth_router

app = FastAPI(title="Auth Microservice")

app.include_router(auth_router)
