from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext

from .base import BaseRepository

from ..schemas.client import ClientCreate, ClientBase, ClientInDB


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

class ClientRepository(BaseRepository):

    async def create_client(self, *, new_client:ClientCreate) -> ClientInDB:

        new_client.password = get_password_hash(new_client.password)
        query_values = new_client.dict()
        client = await self.db.add(table='client', values=query_values)
        self.db.commit()

        return ClientInDB(**client)

    async def get_clients(self) -> List[ClientInDB]:

        SELECT_ALL_USERS_QUERY = """
            SELECT c.id, c.login, c.name, c.email, c.commission, c.is_active,
            r.name as role, o.name as organization_name, o.id as organization_id
            FROM client c
            LEFT JOIN organization_client oc ON c.id = oc.client_id
            LEFT JOIN organization o ON oc.organization_id = o.id
            LEFT JOIN role r ON r.id = oc.role_id
        """

        clients = await self.db.fetch_all(query=SELECT_ALL_USERS_QUERY)

        print([{**client} for client in clients])
        if not clients:
            raise HTTPException(status_code=404, detail="Client not found")
        return [{**client} for client in clients]

    async def get_client(self, id: int) -> ClientInDB:

        SELECT_CLIENT_QUERY = """
            SELECT id, login, name, email, commission, is_active
            FROM client
            WHERE id = :id;
        """

        client = await self.db.fetch_one( query=SELECT_CLIENT_QUERY, values={'id': id} )
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        return {**client}

    async def delete_client(self, id: int) -> ClientInDB:

        DELETE_CLIENT_QUERY = """
            DELETE FROM client WHERE id = :id
            RETURNING id;
        """

        res = await self.db.execute( query=DELETE_CLIENT_QUERY, values={'id': id} )
        print(res)
        if not res:
            raise HTTPException(status_code=404, detail="Client not found")
        return {'response': 'client deleted', 'id': id}

    async def update_client_commission(self, id: int, commission: float) -> ClientInDB:

        UPDATE_CLIENT_COMMISSION_QUERY = """
            UPDATE client SET commission = :commission
            WHERE id = :id
            RETURNING id, login, name, email, commission, is_active;
        """

        client = await self.db.fetch_one( query=UPDATE_CLIENT_COMMISSION_QUERY, values={'id': id, 'commission': commission} )

        if not client:
            raise HTTPException(status_code=404, detail="Client not found")

        return {**client}

    async def update_client_status(self, id: int, is_active: bool) -> ClientInDB:

        UPDATE_CLIENT_STATUS_QUERY = """
            UPDATE client SET is_active = :is_active
            WHERE id = :id
            RETURNING id, login, name, email, commission, is_active;
        """

        client = await self.db.fetch_one( query=UPDATE_CLIENT_STATUS_QUERY, values={'id': id, 'is_active': is_active} )
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        return {**client}

    async def update_client_password(self, id: int, old_password:str, new_password: str) -> ClientInDB:

        UPDATE_CLIENT_PASSWORD_QUERY = """
            UPDATE client SET password = :password
            WHERE id = :id
            RETURNING id, login, name, email, commission, is_active;
        """

        GET_CURRENT_PASSWORD_QUERY ="""
            SELECT password FROM client
            WHERE id = :id;
        """

        current_password = await self.db.fetch_one(query=GET_CURRENT_PASSWORD_QUERY, values={'id': id})

        if not verify_password(old_password, current_password['password']):
            raise HTTPException(status_code=400, detail="Wrong password")

        client = await self.db.fetch_one( query=UPDATE_CLIENT_PASSWORD_QUERY, values={'id': id, 'password': get_password_hash(new_password)} )
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        return {'response': 'Password updated'}

