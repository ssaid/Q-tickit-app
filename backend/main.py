#third imports
from fastapi import FastAPI
from sqlalchemy.orm import Session

#own imports
from config.db import engine, SessionLocal
import models


for model in models.__all__:
    model.Base.metadata.create_all(bind=engine)



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
