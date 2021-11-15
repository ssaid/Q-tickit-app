#third imports
from fastapi import FastAPI
from sqlalchemy.orm import Session

#own imports
from config.db import engine, SessionLocal
from models.models import all_modules



for model in all_modules:
    model.Base.metadata.create_all(bind=engine)



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
