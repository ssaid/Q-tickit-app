from fastapi import APIRouter, Depends, status, Body, HTTPException
from fastapi.exceptions import HTTPException
from typing import List, ForwardRef

from ..repositories.event import EventRepository
from ..dependencies.database import get_repository
from ...models.models import *


router = APIRouter()


@router.post('/', response_model=Event, status_code=status.HTTP_201_CREATED)
def create_event(
    event: EventCreate,
    event_repository: EventRepository = Depends(get_repository(EventRepository))):

    return event_repository.create_event(new_event=event)

