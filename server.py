from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "name": "Task",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }, 200

@app.get("/health")
def get_health():
    return {
        "status": "ok"
    }, 200

