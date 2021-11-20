
from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from typing import List

from .base import BaseRepository

from ..models import user as models


class UserRepository(BaseRepository):

    async def get_user(self, *, id: int) -> models.User:
        user = await self.db.query(models.User).filter(models.User.id == id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user