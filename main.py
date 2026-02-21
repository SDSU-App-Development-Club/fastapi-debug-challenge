from fastapi import FastAPI

app = FastAPI()


# How does FastAPI usually expect you to describe a request body with multiple fields?

@app.post("/items/")
def create_item(name: str, price: float):
    return {"name": name, "price": price}
