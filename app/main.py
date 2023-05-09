from fastapi import FastAPI

app = FastAPI()

from modules.users.router import UserRouter
#print(app)
router = UserRouter()
app.include_router(router.router)

@app.get("/")
def read_root():
    return {"Hello":"World"}
