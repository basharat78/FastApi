from fastapi import APIRouter 
from app.schemas.auth_schma import LoginRequest
router = APIRouter(
    prefix="/auth",
    tags=["auth"])
@router.post("/login")
def login(login_request: LoginRequest):
    return {
    "message": "Login request received",
    "login": login_request.login
}
