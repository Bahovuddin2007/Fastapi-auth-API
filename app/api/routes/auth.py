from fastapi import APIRouter
from pydantic import BaseModel

from app.core.security import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

class LoginRequest(BaseModel):
    username: str

@router.post("/login")
def login(payload: LoginRequest):
    token = create_access_token({"sub": payload.username})
    return {"access_token": token, "token_type": "bearer"}
