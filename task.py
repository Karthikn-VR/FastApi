from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


app = FastAPI()

class task(BaseModel):
    title : str
    year : int

@app.post("/create")
def create(task:task):
    return {"data":f"Creatededdd {task.title}"}

@app.post("/created")
def create(title,year):
    return {"data":title, year:"Creatededdd"}

# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.0.1", port=9000)