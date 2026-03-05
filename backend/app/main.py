from fastapi import FastAPI
from app.routes import auth, logs, ai

app = FastAPI()

app.include_router(auth.router)
app.include_router(logs.router)
app.include_router(ai.router)

@app.get("/")
def read_root():
    return {"message": "CloudSec AI backend is running!!"}