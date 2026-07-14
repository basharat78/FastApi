from fastapi import APIRouter
from app.core.security import verify_password
from app.schemas.auth_schma import LoginRequest
from app.database.user import users

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post("/login")
def login(login_request: LoginRequest):
    for user in users:
        if user["login"] == login_request.login:
            if verify_password(
                login_request.password,
                user["password"]
            ):
                return {
                    "message": "Login successful",
                    "user": user["login"]
                }

            return {
                "message": "Invalid password"
            }

    return {
        "message": "User not found"
    }