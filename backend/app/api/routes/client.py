from fastapi import APIRouter, Depends, status, Body, HTTPException
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..repositories.client import ClientRepository
from ..dependencies.database import get_database, get_repository

from ..schemas.client import *


router = APIRouter()


@router.get("/", response_model=List[ClientInDB])
async def get_clients(
    client_repo: ClientRepository = Depends(get_repository(ClientRepository))
    ):
    clients = await client_repo.get_clients()
    if not clients:
        raise HTTPException(status_code=404, detail="Clients not found")
                          
    return clients

@router.get("/{id}", response_model=ClientInDB)
async def get_client(
    id: int,
    client_repo: ClientRepository = Depends(get_repository(ClientRepository))
    ) -> ClientInDB:
    client = await client_repo.get_client(id)
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
                          
    return client

@router.post("/", response_model=ClientInDB, status_code=status.HTTP_201_CREATED)
async def create_client(
    new_client: ClientCreate,
    client_repo: ClientRepository = Depends(get_repository(ClientRepository))
    ):
    print(new_client)
    client = await client_repo.create_client(new_client=new_client)
    return client

@router.delete("/{id}", responses={204: {'response': 'client deleted', 'id': id}})
async def delete_client(
    id: int,
    client_repo: ClientRepository = Depends(get_repository(ClientRepository))
    ):
    res = await client_repo.delete_client(id)
    if not res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
                          
    return res

@router.put("/{id}/commission", response_model=ClientInDB)
async def update_client_commission(
    id: int,
    commission: CommissionUpdate,
    client_repo: ClientRepository = Depends(get_repository(ClientRepository))
    ):
    client = await client_repo.update_client_commission(id, commission.commission)
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
                          
    return client

@router.put("/{id}/status", response_model=ClientInDB)
async def update_client_status(
    id: int,
    is_active: StatusUpdate,
    client_repo: ClientRepository = Depends(get_repository(ClientRepository))
    ):
    client = await client_repo.update_client_status(id, is_active.is_active)
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
                          
    return client

@router.put("/{id}")
async def update_client_password(
    id: int,
    request: PasswordUpdate,
    client_repo: ClientRepository = Depends(get_repository(ClientRepository))
    ):
    res = await client_repo.update_client_password(id, request.old_password, request.new_password)
    if not res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
                          
    return res