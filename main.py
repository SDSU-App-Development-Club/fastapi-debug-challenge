from fastapi import FastAPI

app = FastAPI()


@app.get("/status")
def get_status():
    status = {"status": "running", "version": "1.0"}
