from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop"},
    {"id": 2, "name": "Mouse"},
]


@app.get("/products/{product_id}")
def get_product(product_id: str):
    for product in products:
        if product["id"] == product_id:  
            return product
    return {"error": "Product not found"}
