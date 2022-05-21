from fastapi import APIRouter, Depends, status, Body, HTTPException
from fastapi.exceptions import HTTPException
from typing import List

from ..repositories.organization import OrganizationRepository
from ..dependencies.database import get_repository
from ...models.models import *


router = APIRouter()


@router.post('/', response_model=Organization, status_code=status.HTTP_201_CREATED)
async def create_organization(
    organization: OrganizationCreate,
    organization_repository: OrganizationRepository = Depends(
        get_repository(OrganizationRepository))
    ):
    return await organization_repository.create_organization(new_organization=organization)

@router.get('/get_organization_by_id', response_model=OrganizationRead)
async def get_organization(
    organization_id: int,
    organization_repository: OrganizationRepository = Depends(
        get_repository(OrganizationRepository))
    ):
    res = await organization_repository.get_organization(organization_id=organization_id)


    return res


@router.get('/get_organization_by_user/{user_id}', response_model=List[OrganizationRead])
async def get_organization_of_user(
    user_id: int,
    organization_repository: OrganizationRepository = Depends(
        get_repository(OrganizationRepository))
    ):
    res = await organization_repository.get_organizations_for_user(user_id=user_id)
    return res

@router.post('/add_user', response_model=OrganizationRead)
async def add_user_to_organization(
    organization_id: int,
    user_id: int,
    permissions: str = None,
    organization_repository: OrganizationRepository = Depends(
        get_repository(OrganizationRepository))
    ):

    return await organization_repository.add_user(organization_id=organization_id, user_id=user_id, role_id=role_id)
