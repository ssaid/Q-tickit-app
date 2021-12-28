from fastapi import APIRouter

from .client import router as client_router


router = APIRouter()


router.include_router(client_router, prefix="/clients", tags=["clients"])

