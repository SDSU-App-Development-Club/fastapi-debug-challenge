from fastapi import FastAPI, HTTPException

app = FastAPI()

users_db = {
    1: {"name": "Alice"},
    2: {"name": "Bob"}
}

# This code will run, but that's not the bug we're looking for. 

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users_db:
        # Try requesting /users/999 and check what status code you get. Is it the right one?
        raise HTTPException(status_code=500, detail="User not found")
    return users_db[user_id]
