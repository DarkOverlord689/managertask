from fastapi import APIRouter, HTTPException
from models import LoginInput
from auth_utils import authenticate_user, create_access_token
from datetime import timedelta

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/token")
def login(credentials: LoginInput):
    user = authenticate_user(credentials.email, credentials.password)
    if not user:
        raise HTTPException(status_code=401, detail="Correo o contraseña incorrectos")
    
    access_token = create_access_token(
        data={"sub": user["email"]},  # También puedes incluir "id" o "role"
        expires_delta=timedelta(minutes=30)
    )
    return {"access_token": access_token, "token_type": "bearer"}
