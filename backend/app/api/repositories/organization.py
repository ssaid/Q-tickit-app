from typing import List
from sqlmodel import select
from sqlalchemy.orm import joinedload

from .base import BaseRepository
from ...models.models import *


class OrganizationRepository(BaseRepository):

    async def create_organization(self, *, new_organization: OrganizationCreate) -> Organization:

        organization = Organization(**new_organization.dict())

        self.db.add(organization)

        await self.db.commit()
        await self.db.refresh(organization)

        return organization

    async def get_organization(self, *, organization_id: int) -> OrganizationRead:

        res = await self.db.execute(select(Organization).where(Organization.id == organization_id).options(
                                        joinedload(Organization.users),
                                        joinedload(Organization.events))
                                    )
        organization = res.scalars().first()


        if not organization:
            raise HTTPException(status_code=404, detail="Organization not found")


        users = []
        for link in organization.users:
            user = await self.db.get(User, link.user_id)
            role = await self.db.get(Role, link.role_id)
            user = UserReadInOrganization(**{**user.dict(), 'role': role.name if role else ''})
            users.append(user)


        return {
            **organization.dict(),
            'events': [event.dict() for event in organization.events],
            'users': users
        }

    async def get_organizations(self) -> List[Organization]:

        res = await self.db.execute(select(Organization).options(
                                        joinedload(Organization.users),
                                        joinedload(Organization.events))
                                    )
        organizations = res.scalars()

        return [{**organization.dict(), 'events': [event.dict() for event in organization.events]} for organization in organizations]


    async def add_user(self, *, organization_id: int, user_id: int, role_id: int) -> Organization:


        organization = await self.db.get(Organization, organization_id)
        user = await self.db.get(User, user_id)
        role = await self.db.get(Role, role_id)

        link = OrganizationUserLink(organization=organization, user=user, role=role)

        self.db.add(link)
        await self.db.commit()
        await self.db.refresh(organization)

        return await self.get_organization(organization_id=organization_id)
