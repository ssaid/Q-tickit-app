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

        res = await self.db.execute(select(User).where(User.id == id).options(joinedload(User.events)))
        user = res.scalars().first()

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return {**user.dict(), 'events': [event.dict() for event in user.events]}


    async def get_users(self) -> List[UserRead]:

        print("ESTA ES LA QUERY")
        print(select(User))
        res = await self.db.execute(select(User))
        users = res.scalars().all()

        if not users:
            raise HTTPException(status_code=404, detail="User not found")

        return [UserRead(**user.dict()) for user in users]


    # async def delete_user(self, id: int) -> UserInDB:

    #     res = await self.db.execute( query=DELETE_CLIENT_QUERY, values={'id': id} )
    #     print(res)
    #     if not res:
    #         raise HTTPException(status_code=404, detail="User not found")
    #     return {'response': 'user deleted', 'id': id}

    # async def update_user_commission(self, id: int, commission: float) -> UserInDB:

    #     UPDATE_CLIENT_COMMISSION_QUERY = """
    #         UPDATE user SET commission = :commission
    #         WHERE id = :id
    #         RETURNING id, login, name, email, commission, is_active;
    #     """

    #     user = await self.db.fetch_one( query=UPDATE_CLIENT_COMMISSION_QUERY, values={'id': id, 'commission': commission} )

    #     if not user:
    #         raise HTTPException(status_code=404, detail="User not found")

    #     return {**user}

    # async def update_user_status(self, id: int, is_active: bool) -> UserInDB:

    #     UPDATE_CLIENT_STATUS_QUERY = """
    #         UPDATE user SET is_active = :is_active
    #         WHERE id = :id
    #         RETURNING id, login, name, email, commission, is_active;
    #     """

    #     user = await self.db.fetch_one( query=UPDATE_CLIENT_STATUS_QUERY, values={'id': id, 'is_active': is_active} )
    #     if not user:
    #         raise HTTPException(status_code=404, detail="User not found")
    #     return {**user}

    # async def update_user_password(self, id: int, old_password:str, new_password: str) -> UserInDB:

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

