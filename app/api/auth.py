from fastapi import APIRouter 
from app.schemas.auth_schma import LoginRequest
from app.database.user import users

router = APIRouter(
    prefix="/auth",
    tags=["auth"])
@router.post("/login")
def login(login_request: LoginRequest):
  for user in users:
    if user["login"] == login_request.login and user["password"] == login_request.password:
      return {"message": "Login successful"}
  return {"message": "Invalid login or password"}
