from fastapi import FastAPI, Depends

app = FastAPI()


def get_current_user():
    return {"username": "testuser"}


@app.get("/profile")
def read_profile(user: dict = Depends(get_current_user)):
    return {"user": user}


@app.get("/settings")
def read_settings():
    # Bug: Trying to use 'user' without declaring it
    return {"user": user, "settings": {}}
