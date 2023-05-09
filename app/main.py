from fastapi import FastAPI
from config.db import conn

app = FastAPI()

from modules.users.router import UserRouter
#print(app)


router = UserRouter(conn)
app.include_router(router.router)

@app.get("/")
def read_root():
    return {"Hello":"World"}
