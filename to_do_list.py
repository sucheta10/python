#Simple to-do-list using fastapi
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    task_name: str

tasks = []

@app.get("/")
async def read_root():
    return {"message": "Welcome to the To-Do List API!"}

@app.post("/tasks/")
async def create_task(task: Task):
    task_id = len(tasks)
    tasks.append(task.task_name)
    save_tasks_to_file()
    return {"message": "Task added successfully", "task_id": task_id}

@app.get("/tasks/")
async def get_tasks():
    return {"tasks": tasks}

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    save_tasks_to_file()
    return {"message": "Task deleted successfully"}

def save_tasks_to_file():
    with open("tasklist.txt", 'w') as taskfile:
        for task in tasks:
            taskfile.write(task + "\n")
