from fastapi import FastAPI
from pydantic import BaseModel

class Task(BaseModel):
    title: str
    done: bool
  

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
            return task, 200

    return {"error": f"Task {id} not found"}, 404    

@app.post("/task")
def create_task(task: Task):

    if not task.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Bad Request"
        )

    total = len(tasks)

    newTask = {
        "id": total + 1,
        "title": task.title,
        "done": False
    }
    tasks.append(newTask)

    return {
        "message": "Task created successfully",
        "task": task
    }

@app.put("/task/{id}")
def update_task(id: int, task_update: Task):

    for task in tasks:
        if task["id"] == id:

            update_data = task_update.model_dump(exclude_unset=True)


           
            if not update_data:
                raise HTTPException(
                    status_code=400,
                    detail="No fields provided for update"
            )

            if "title" in update_data and not update_data["title"].strip():
                raise HTTPException(
                    status_code=400,
                    detail="Title cannot be empty"
            )
            
            task.update(update_data)

            return task

    raise HTTPException(
    status_code=404,
    detail="Task not found"
    )


@app.delete("/task/{id}")
def delete_task(id: int):

    for task in tasks:
        if task["id"] == id:
            task.pop
            return {"message": f"Successfully remove {task["title"]}"}
        
    raise HTTPException(
    status_code=404,
    detail="Task not found"
    )
