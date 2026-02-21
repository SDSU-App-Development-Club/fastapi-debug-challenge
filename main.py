from fastapi import FastAPI, Depends

app = FastAPI()


def get_current_user():
    return {"username": "testuser"}


@app.get("/profile")
def read_profile(user: dict = Depends(get_current_user)):
    return {"user": user}


# How does read_profile get "user"? Does read_settings get it the same way?
@app.get("/settings")
def read_settings():
    return {"user": user, "settings": {}}
