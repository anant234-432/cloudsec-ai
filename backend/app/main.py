from fastapi import FastAPI
from app.routes import auth, logs, ai
from app.database import engine
from app.database import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(logs.router)
app.include_router(ai.router)

@app.get("/")
def read_root():
    return {"message": "CloudSec AI backend is running!!"}