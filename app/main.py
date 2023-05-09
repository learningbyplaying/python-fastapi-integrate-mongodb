from fastapi import FastAPI


app = FastAPI()
#print(app)

@app.get("/")
def read_root():
    return {"Hello":"World"}
