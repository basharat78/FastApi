from fastapi import FastAPI
from app.api.auth import router as auth_router



app = FastAPI(
    title="Students HUB",
)

app.include_router(auth_router)
@app.get('/')
def home():
    return {"message": "Welcome to Students HUB!"}

