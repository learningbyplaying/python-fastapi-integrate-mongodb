from fastapi import FastAPI
import db

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/all")
def get_all():
    data = db.all()
    return {"data": data}

@app.post("/create")
def create(data):
    id = db.create(data)
    return {'inserted': True, "inserted_id": id}
