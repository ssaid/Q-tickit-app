from fastapi import APIRouter, Depends, status, Body, HTTPException
from fastapi.exceptions import HTTPException
from typing import List, ForwardRef

from ..repositories.user import UserRepository
from ..dependencies.database import get_repository
from ...models.models import *


router = APIRouter()


#TODO: ver por que no funciona con async algunas querys
#TODO: que onda con los circular imports en los models ?? (no funciona TYPE_CHECKING??)

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(
    new_user: UserCreate,
    user_repo: UserRepository = Depends(get_repository(UserRepository))
    ):

    return await user_repo.create_user(new_user=new_user)


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



# @router.delete("/{id}", responses={204: {'response': 'user deleted', 'id': id}})
# async def delete_user(
#     id: int,
#     user_repo: UserRepository = Depends(get_repository(UserRepository))
#     ):
#     res = await user_repo.delete_user(id)
#     if not res:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

#     return res

# @router.put("/{id}/commission", response_model=UserInDB)
# async def update_user_commission(
#     id: int,
#     commission: CommissionUpdate,
#     user_repo: UserRepository = Depends(get_repository(UserRepository))
#     ):
#     user = await user_repo.update_user_commission(id, commission.commission)
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

#     return user

# @router.put("/{id}/status", response_model=UserInDB)
# async def update_user_status(
#     id: int,
#     is_active: StatusUpdate,
#     user_repo: UserRepository = Depends(get_repository(UserRepository))
#     ):
#     user = await user_repo.update_user_status(id, is_active.is_active)
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

#     return user

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
