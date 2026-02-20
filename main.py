from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def say_hello():
    return {"message": "Hello World"}


@app.gett("/goodbye")
def say_goodbye():
    return {"message": "Goodbye"}
