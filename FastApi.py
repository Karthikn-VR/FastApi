from fastapi import FastAPI,Path
from pydantic import BaseModel

app=FastAPI()

inven = {
    1: {
        "name" : "Karthi",
        "id"    : 63,
        "dob" : 2004
        }
}

@app.get("/")
def home():
    return{"Welcome to FastApi":"Home"}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(...,discription="the item u touched")):
    return inven[item_id]

@app.get("/get-id")
def get_id(name:str = None):
    for item_id in inven:
        if inven[item_id]["name"] == name:
            return inven[item_id]
    return {"Data":"Not found"}

