from fastapi import APIRouter, Depends, status, Body, HTTPException
from fastapi.exceptions import HTTPException
from typing import List

from ..repositories.role import RoleRepository
from ..dependencies.database import get_repository
from ...models.models import *


router = APIRouter()


@router.post('/', response_model=Role, status_code=status.HTTP_201_CREATED)
async def create_role(
    role: RoleCreate,
    role_repository: RoleRepository = Depends(
        get_repository(RoleRepository))
    ):

    return await role_repository.create_role(new_role=role)

