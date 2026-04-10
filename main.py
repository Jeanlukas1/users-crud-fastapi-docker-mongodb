from fastapi import FastAPI
from src.routes.user_routes import router

app = FastAPI(title="Users CRUD", description="Users management developed with FastAPI to manage the apis, docker and MongoDB to persist the datas.")
app.include_router(router)

@app.get("/")
def home():

    return {"message": "FastAPI + MongoDB + Docker"}