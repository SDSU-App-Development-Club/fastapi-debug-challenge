from fastapi import FastAPI
import time

app = FastAPI()


# In async code, does time.sleep let other work run while waiting?
async def slow_operation():
    time.sleep(2)
    return {"status": "complete"}


@app.get("/process")
async def process_data():
    # Calling an async function - do you get a value back immediately or something else?
    result = slow_operation()
    return result
