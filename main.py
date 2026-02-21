from fastapi import FastAPI

app = FastAPI()

users = []

# Same thing here, the code will run but you need to go into Swagger UI to see what's really wrong. 
# Unless you can see it directly from here.


@app.get("/users")
def create_user(name: str):
    users.append({"name": name})
    return {"message": "User created"}
