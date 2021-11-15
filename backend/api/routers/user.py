from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from ..schemas import user as schemas
from ..config.database import get_db

router = APIRouter()


@router.get("/{id}", response_model=schemas.ShowUser)
async def get_users(id: int, db: Session = Depends(get_db)):
    user = db.query(schemas.User).filter(schemas.User.id == id).first()
    return user

@router.get("/", response_model=List[schemas.ShowUser])
async def get_users(db: Session = Depends(get_db)):
    users = db.query(schemas.User).all()
    return users

@router.post("/", response_model=schemas.ShowUser)
async def create_user(user: schemas.User, db: Session = Depends(get_db)):
    db_user = db.query(schemas.User).filter(schemas.User.username == user.username).first()
    if db_user:
        raise Exception("User already exists")
    db_user = schemas.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
