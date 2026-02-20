from fastapi import FastAPI

app = FastAPI()

users = []


@app.get("/users")
def create_user(name: str):
    users.append({"name": name})
    return {"message": "User created"}
