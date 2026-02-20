from fastapi import FastAPI

app = FastAPI()


@app.post("/items/")
def create_item(name: str, price: float):
    return {"name": name, "price": price}
