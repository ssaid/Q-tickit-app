from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from typing import List

from .base import BaseRepository

from ..schemas.client import ClientCreate, ClientBase, ClientInDB

CREATE_USER_QUERY = """
    INSERT INTO client (login, name, email, commission, is_active, password)
    VALUES (:login, :name, :email, :commission, :is_active, :password)
    RETURNING id, login, name, email, commission, is_active;
"""

SELECT_ALL_USERS_QUERY = """
    SELECT id, login, name, email, commission, is_active
    FROM client; 
"""

SELECT_CLIENT_QUERY = """
    SELECT id, login, name, email, commission, is_active
    FROM client
    WHERE id = :id; 
"""

class ClientRepository(BaseRepository):

    async def create_client(self, *, new_client:ClientCreate) -> ClientInDB:
        query_values = new_client.dict()
        client = await self.db.fetch_one(query=CREATE_USER_QUERY, values=query_values)
        return ClientInDB(**client)

    async def get_clients(self) -> List[ClientInDB]:
        
        clients = await self.db.fetch_all(query=SELECT_ALL_USERS_QUERY)
        if not clients:
            raise HTTPException(status_code=404, detail="Client not found")
        return [{**client} for client in clients]

    async def get_client(self, id: int) -> ClientInDB:

        client = await self.db.fetch_one( query=SELECT_CLIENT_QUERY, values={'id': id} )
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        return {**client}
