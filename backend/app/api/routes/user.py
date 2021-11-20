from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from typing import List

# from ..repositories.user import UserRepository
# from api.dependencies import get_repository

# from ..schemas import user as schemas
# from ..config.database import get_db
# from ..models import user as models


router = APIRouter()


@router.get("/{id}")#, response_model=schemas.User)
async def get_user(id: int):
    return id
    # id: int, 
    # user_repo: UserRepository = Depends(get_repository(UserRepository))
    # ) -> schemas.User:
    # user = await user_repo.get_user(id=id)
    # return user

# @router.get("/", response_model=List[schemas.User])
# async def get_users(db: Session = Depends(get_db)):
#     users = db.query(models.User).all()
#     if not users:
#         raise HTTPException(status_code=404, detail="Users not found")
#     return users

# @router.post("/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
# async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = db.query(models.User).filter(models.User.username == user.username).first()
#     if db_user:
#         raise Exception("User already exists")
#     db_user = models.User(**user.dict())
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
