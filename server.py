from fastapi import FastAPI

app = FastAPI()

tasks = [
    {
        "id": 1,
        "title": "Learn Python",
        "done": False
    },
    {
        "id": 2,
        "title": "Study FastAPI",
        "done": False
    },
    {
        "id": 3,
        "title": "Build CRUD API",
        "done": True
    }
]

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

@app.get("/task")
def get_all():

    if tasks is None:
        return {"message": "No task"}
     
    return tasks

@app.get("/task/{id}")
def get_task(id: int):

    for task in tasks:
        if task["id"] == id:
            return task

    return {"error": f"Task {id} not found"}, 404    
