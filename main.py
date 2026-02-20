from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserResponse(BaseModel):
    username: str
    email: str


@app.get("/user", response_model=UserResponse)
def get_user():
    return {
        "username": "alice",
        "email": "alice@example.com",
        "password": "secret123"
    }
