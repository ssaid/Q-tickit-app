from fastapi import APIRouter, Depends, status, Body, HTTPException
from fastapi.exceptions import HTTPException
from typing import List, ForwardRef

from ..repositories.user import UserRepository
from ..dependencies.database import get_repository
from ...models.models import *


router = APIRouter()


#TODO: ver por que no funciona con async algunas querys
#TODO: que onda con los circular imports en los models ?? (no funciona TYPE_CHECKING??)

@router.post("/", response_model=UserAuthenticated, status_code=status.HTTP_201_CREATED)
async def create_user(
    new_user: UserCreate,
    user_repo: UserRepository = Depends(get_repository(UserRepository))
    ):

    return await user_repo.create_user(new_user=new_user)

@router.post("/authenticate", response_model=UserAuthenticated)
async def authenticate_user(
    credentials: UserCredentials,
    user_repo: UserRepository = Depends(get_repository(UserRepository))
    ) -> UserAuthenticated:
    user: UserValidation = await user_repo.get_user_by_login(login=credentials.login)
    if not user:
        raise HTTPException(status_code=403, detail="Credentials Not Valid")
    print(user)
    print('--')
    print(credentials)
    is_valid = user_repo.check_credentials(encrypted_password=user.password, plain_password=credentials.password)

    if not is_valid:
        raise HTTPException(status_code=403, detail="Credentials Not Valid")

    jwt_token, expiry_date = user_repo.create_access_token(user.login)

    return UserAuthenticated(token=jwt_token, expiration=expiry_date, user_id=user.id)


@router.get("/{id}", response_model=UserReadWithRelationships)
async def get_user(
    id: int,
    user_repo: UserRepository = Depends(get_repository(UserRepository))
    ) -> UserReadWithRelationships:

    return await user_repo.get_user(id)


@router.get("/", response_model=List[UserRead])
async def get_users(
    user_repo: UserRepository = Depends(get_repository(UserRepository))
    ):
    users = await user_repo.get_users()
    if not users:
        raise HTTPException(status_code=404, detail="Users not found")

    return users



@router.delete("/{id}")
async def delete_user(
    id: int,
    user_repo: UserRepository = Depends(get_repository(UserRepository))
    ):
    await user_repo.delete_user(id)

    return {"message": "User deleted"}

@router.put("/{id}/commission", response_model=UserRead)
async def update_user_commission(
    request: UserCommission,
    user_repo: UserRepository = Depends(get_repository(UserRepository))
    ):
    user = await user_repo.update_user_commission(request.id, request.commission)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return user

@router.put("/{id}/status", response_model=UserRead)
async def update_user_status(
    request: UserIsActive,
    user_repo: UserRepository = Depends(get_repository(UserRepository))
    ):

    return await user_repo.update_user_status(request.id, request.is_active)

# @router.put("/{id}")
# async def update_user_password(
#     id: int,
#     request: PasswordUpdate,
#     user_repo: UserRepository = Depends(get_repository(UserRepository))
#     ):
#     res = await user_repo.update_user_password(id, request.old_password, request.new_password)
#     if not res:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

#     return res
