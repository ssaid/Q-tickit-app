from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List, Optional
from passlib.context import CryptContext
from sqlmodel import select
from datetime import timedelta
from datetime import datetime

from .base import BaseRepository
from ...models.models import *

from jose import JWTError, jwt
from ...db.config import SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = timedelta(minutes=30)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

class UserRepository(BaseRepository):
    def create_access_token(self, user: str, expires_delta: Optional[timedelta] = ACCESS_TOKEN_EXPIRE_MINUTES):
        print(SECRET_KEY)
        expire = datetime.utcnow() + expires_delta
        to_encode = {'user': user, 'exp': expire}
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt, expire

    def create_user(self, *, new_user: UserCreate) -> UserAuthenticated:

        new_user.password = get_password_hash(new_user.password)
        query_values = new_user.dict()
        user = User(**query_values)

        self.db.add(user)
        self.db.commit()

        self.db.refresh(user)

        jwt_token, expiry_date = self.create_access_token(user.login)

        return UserAuthenticated(token=jwt_token, expiration=expiry_date, user_id=user.id)


    def get_user_by_login(self, *, login: str) -> UserValidation:
        res = self.db.execute(select(User).where(User.login == login))
        user = res.scalars().first()

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return UserValidation(**user.dict())

    def check_credentials(self, *, encrypted_password, plain_password) -> bool:
        return verify_password(plain_password, encrypted_password)


    def get_user(self, id: int) -> UserReadWithRelationships:

        res = self.db.execute(select(User).where(User.id == id).options(
                                        joinedload(User.organizations),
                                        joinedload(User.events))
                                    )
        user = res.scalars().first()

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return {**user.dict(), 'events': [event.dict() for event in user.events]}


    def get_users(self) -> List[UserRead]:

        res = self.db.execute(select(User))
        users = res.scalars().all()

        if not users:
            raise HTTPException(status_code=404, detail="User not found")

        return [UserRead(**user.dict()) for user in users]


    def delete_user(self, id: int) -> None:

        user = self.db.get(User, id)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        self.db.delete(user)
        self.db.commit()


    def update_user_commission(self, id: int, commission: float) -> UserRead:

        user = self.db.get(User, id)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        user.commission = commission

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return {**user.dict()}

    def update_user_status(self, id: int, is_active: bool) -> UserRead:

        user = self.db.get(User, id)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        user.is_active = is_active

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return {**user.dict()}

    # def update_user_password(self, id: int, old_password:str, new_password: str) -> UserRead:

    #     UPDATE_CLIENT_PASSWORD_QUERY = """
    #         UPDATE user SET password = :password
    #         WHERE id = :id
    #         RETURNING id, login, name, email, commission, is_active;
    #     """

    #     GET_CURRENT_PASSWORD_QUERY ="""
    #         SELECT password FROM user
    #         WHERE id = :id;
    #     """

    #     current_password = self.db.fetch_one(query=GET_CURRENT_PASSWORD_QUERY, values={'id': id})

    #     if not verify_password(old_password, current_password['password']):
    #         raise HTTPException(status_code=400, detail="Wrong password")

    #     user = self.db.fetch_one( query=UPDATE_CLIENT_PASSWORD_QUERY, values={'id': id, 'password': get_password_hash(new_password)} )
    #     if not user:
    #         raise HTTPException(status_code=404, detail="User not found")
    #     return {'response': 'Password updated'}

