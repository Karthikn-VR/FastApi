from fastapi import FastAPI

app = FastAPI()

datas = {
    1: {
        "name" : "karthi",
        "id" : 67
    }
}

@app.get("/get-name")
def home(name : str):
    for data_id in datas:
        if datas[data_id]["name"]==name:
            return datas[data_id]
    return {"error":"not found"}    