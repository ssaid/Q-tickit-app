from fastapi import APIRouter

from .user import router as user_router
from .event import router as event_router


router = APIRouter()


router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(event_router, prefix="/events", tags=["events"])

