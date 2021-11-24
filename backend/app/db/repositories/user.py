
from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from typing import List

from .base import BaseRepository

from ...schemas.user import UserCreate, UserBase, UserInDB

CREATE_USER_QUERY = """
    INSERT INTO public.user (login, name, email, commission, is_active, password)
    VALUES (:login, :name, :email, :commission, :is_active, :password)
    RETURNING id, login, name, email, commission, is_active;
"""

SELECT_ALL_USERS_QUERY = """
    SELECT id, login, name, email, commission, is_active
    FROM public.user; 
"""

class UserRepository(BaseRepository):

    async def create_user(self, *, new_user:UserCreate) -> UserInDB:
        query_values = new_user.dict()
        print(query_values)
        user = await self.db.fetch_one(query=CREATE_USER_QUERY, values=query_values)
        print("===========USER===========")
        print(user)
        return UserInDB(**user)

    async def get_users(self) -> List[UserInDB]:
        
        users = await self.db.fetch_all(query=SELECT_ALL_USERS_QUERY)
        if not users:
            raise HTTPException(status_code=404, detail="User not found")
        return [{**user} for user in users]