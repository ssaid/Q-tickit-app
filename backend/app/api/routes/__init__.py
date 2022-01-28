from fastapi import APIRouter

from .user import router as user_router
from .event import router as event_router
from .organization import router as organization_router
from .role import router as role_router


router = APIRouter()


router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(event_router, prefix="/events", tags=["events"])
router.include_router(organization_router, prefix="/organizations", tags=["organizations"])
router.include_router(role_router, prefix="/roles", tags=["roles"])

