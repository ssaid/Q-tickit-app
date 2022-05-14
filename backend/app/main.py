from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db.db import init_db
from .models import *
from .api.routes import router as api_router
from .db.config import PROJECT_NAME, VERSION

origins = [
    "http://localhost",
    "http://localhost:3000",
    "*",
]

app = FastAPI(title=PROJECT_NAME, version=VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup():
    pass
    await init_db()


app.include_router(api_router, prefix="/api")
