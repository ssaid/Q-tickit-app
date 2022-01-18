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
DELETE_CLIENT_QUERY = """
    DELETE FROM client WHERE id = :id
    RETURNING id;
"""

UPDATE_CLIENT_COMMISSION_QUERY = """
    UPDATE client SET commission = :commission
    WHERE id = :id
    RETURNING id, login, name, email, commission, is_active;
"""

UPDATE_CLIENT_STATUS_QUERY = """
    UPDATE client SET is_active = :is_active
    WHERE id = :id
    RETURNING id, login, name, email, commission, is_active;
"""

UPDATE_CLIENT_PASSWORD_QUERY = """
    UPDATE client SET password = :password
    WHERE id = :id
    RETURNING id, login, name, email, commission, is_active;
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

    async def delete_client(self, id: int) -> ClientInDB:

        res = await self.db.execute( query=DELETE_CLIENT_QUERY, values={'id': id} )
        print(res)
        if not res:
            raise HTTPException(status_code=404, detail="Client not found")
        return {'response': 'client deleted', 'id': id}

    async def update_client_commission(self, id: int, commission: float) -> ClientInDB:

        print(f"id: {id}, commission: {commission}")
        client = await self.db.fetch_one( query=UPDATE_CLIENT_COMMISSION_QUERY, values={'id': id, 'commission': commission} )

        if not client:
            raise HTTPException(status_code=404, detail="Client not found")

        return {**client}

    async def update_client_status(self, id: int, is_active: bool) -> ClientInDB:

        client = await self.db.fetch_one( query=UPDATE_CLIENT_STATUS_QUERY, values={'id': id, 'is_active': is_active} )
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        return {**client}

    async def update_client_password(self, id: int, password: str) -> ClientInDB:

        client = await self.db.fetch_one( query=UPDATE_CLIENT_PASSWORD_QUERY, values={'id': id, 'password': password} )
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        return {'response': 'Password updated'}

