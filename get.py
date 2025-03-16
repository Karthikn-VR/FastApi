from fastapi import FastAPI,Path
from typing import Optional


app = FastAPI()

task_data = {
    1:{
        "Task":"Buy milk",
        "Time" : "4 p.m"
    },
    2:{
        "Task":"cook",
         "time":"5pm"
    }
}




@app.get("/get-task/{task_id}")
def home(task_id :int = Path(..., description="enter Task id",gt=0)):
    return task_data[task_id]


@app.get("/get-by-id/{task_id}")
def get_task(*,task_id: int,Task: Optional[str]=None):
    for task_id in task_data:
        if task_data[task_id]["Task"]== Task:
            return task_data[task_id]
    return {"data":"not found"}    

