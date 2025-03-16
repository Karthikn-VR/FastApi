from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tasks = {
    1:{
        "name" : "grocery",
        "time":"6pm"
    }
}
class task(BaseModel):
    name : str
    time : str

@app.get("/get-item/{task_id}")
def show(task_id: int):
    return tasks[task_id]

@app.post("/create")
def create(task_id :int,task_data:task):
    if task_id in tasks:
        return {"error":"enter a new task"}
    tasks[task_id] = task_data
    return tasks[task_id]