from typing import List
from sqlmodel import select

from .base import BaseRepository
from ...models.models import *


class RoleRepository(BaseRepository):

    async def create_role(self, *, new_role: RoleCreate) -> Role:
        role = Role(**new_role.dict())

        self.db.add(role)

        await self.db.commit()
        await self.db.refresh(role)

        return role


    async def delete_role(self, *, role_id: int) -> None:
        role = await self.db.get(Role, role_id)

        await self.db.delete(role)

        await self.db.commit()

