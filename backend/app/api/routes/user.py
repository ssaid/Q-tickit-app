from fastapi import APIRouter, Depends, status, Body
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from typing import List

from ...db.repositories.user import UserRepository
from ..dependencies.database import get_database, get_repository

from ...schemas.user import UserCreate, UserBase, UserInDB


router = APIRouter()


@router.get("/", response_model=List[UserInDB])
async def get_user(
    user_repo: UserRepository = Depends(get_repository(UserRepository))
    ):
    users = await user_repo.get_users()
    return users

# @router.get("/", response_model=List[schemas.User])
# async def get_users(db: Session = Depends(get_db)):
#     users = db.query(models.User).all()
#     if not users:
#         raise HTTPException(status_code=404, detail="Users not found")
#     return users

@router.post("/", response_model=UserInDB, status_code=status.HTTP_201_CREATED)
async def create_user(
    new_user: UserCreate,
    user_repo: UserRepository = Depends(get_repository(UserRepository))
    ):
    print(new_user)
    user = await user_repo.create_user(new_user=new_user)
    return user
