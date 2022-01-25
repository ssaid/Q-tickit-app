from fastapi import FastAPI

from .db.db import init_db
from .models import *
from .api.routes import router as api_router
from .db.config import PROJECT_NAME, VERSION

app = FastAPI(title=PROJECT_NAME, version=VERSION)


@app.on_event("startup")
async def on_startup():
    await init_db()


app.include_router(api_router, prefix="/api")
