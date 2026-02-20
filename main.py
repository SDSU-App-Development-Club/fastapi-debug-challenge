from fastapi import FastAPI
import time

app = FastAPI()


async def slow_operation():
    time.sleep(2)  # Blocks the entire server!
    return {"status": "complete"}


@app.get("/process")
async def process_data():
    result = slow_operation()  # Missing await
    return result
