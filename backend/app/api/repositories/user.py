from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List
from passlib.context import CryptContext
from sqlmodel import select

from .base import BaseRepository
from ...models.models import *


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

class UserRepository(BaseRepository):

    async def create_user(self, *, new_user: UserCreate) -> UserRead:

        new_user.password = get_password_hash(new_user.password)
        query_values = new_user.dict()
        user = User(**query_values)

        self.db.add(user)
        await self.db.commit()

        await self.db.refresh(user)
        return UserRead(**user.dict())


    async def get_user(self, id: int) -> UserReadWithRelationships:

        res = await self.db.execute(select(User).where(User.id == id).options(
                                        joinedload(User.organizations),
                                        joinedload(User.events))
                                    )
        user = res.scalars().first()

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return {**user.dict(), 'events': [event.dict() for event in user.events]}


    async def get_users(self) -> List[UserRead]:

        res = await self.db.execute(select(User))
        users = res.scalars().all()

        if not users:
            raise HTTPException(status_code=404, detail="User not found")

        return [UserRead(**user.dict()) for user in users]


    async def delete_user(self, id: int) -> None:

        user = await self.db.get(User, id)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        await self.db.delete(user)
        await self.db.commit()


    async def update_user_commission(self, id: int, commission: float) -> UserRead:

        user = await self.db.get(User, id)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        user.commission = commission

        self.db.add(user)
        await self.db.commit()
        self.db.refresh(user)

        return {**user.dict()}

    async def update_user_status(self, id: int, is_active: bool) -> UserRead:

        user = await self.db.get(User, id)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        user.is_active = is_active

        self.db.add(user)
        await self.db.commit()
        self.db.refresh(user)

        return {**user.dict()}

    # async def update_user_password(self, id: int, old_password:str, new_password: str) -> UserRead:

    #     UPDATE_CLIENT_PASSWORD_QUERY = """
    #         UPDATE user SET password = :password
    #         WHERE id = :id
    #         RETURNING id, login, name, email, commission, is_active;
    #     """

    #     GET_CURRENT_PASSWORD_QUERY ="""
    #         SELECT password FROM user
    #         WHERE id = :id;
    #     """

    #     current_password = await self.db.fetch_one(query=GET_CURRENT_PASSWORD_QUERY, values={'id': id})

    #     if not verify_password(old_password, current_password['password']):
    #         raise HTTPException(status_code=400, detail="Wrong password")

    #     user = await self.db.fetch_one( query=UPDATE_CLIENT_PASSWORD_QUERY, values={'id': id, 'password': get_password_hash(new_password)} )
    #     if not user:
    #         raise HTTPException(status_code=404, detail="User not found")
    #     return {'response': 'Password updated'}

