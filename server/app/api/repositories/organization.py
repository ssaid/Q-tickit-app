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

        user = await self.db.get(User, new_organization.user_id)
        permissions = "['home','camera','stats','config','events']"

        link = OrganizationUserLink(organization=organization, user=user, permissions=permissions)

        self.db.add(link)
        await self.db.commit()

        return organization

    async def get_organization(self, *, organization_id: int) -> OrganizationRead:
        res = self.db.execute(select(Organization).where(Organization.id == organization_id).join(Organization.users))
        organization = res.scalars().first()


        if not organization:
            raise HTTPException(status_code=404, detail="Organization not found")


        users = []
        # import wdb; wdb.set_trace()
        for link in organization.users:
            user = await self.db.get(User, link.user_id)
            dd = {
                'id': user.id,
                'name': user.name,
                'is_active': user.is_active,
                'permissions': link.permissions
            }
            user = UserReadInOrganization(**dd)
            users.append(user)


        return {
            **organization.dict(),
            'events': [event.dict() for event in organization.events],
            'users': users
        }
        res = await res
    async def get_organizations_for_user(self, user_id) -> List[Organization]:
        res = await self.db.execute(select(Organization).options(
                                        joinedload(Organization.users, innerjoin=True)).filter_by(user_id=user_id)
                                    )
        organizations = res.scalars()

        return [organization.dict() for organization in organizations.unique()]

    async def get_organizations(self) -> List[Organization]:

        res = await self.db.execute(select(Organization).options(
                                        joinedload(Organization.users),
                                        joinedload(Organization.events))
                                    )
        organizations = res.scalars()

        return [{**organization.dict(), 'events': [event.dict() for event in organization.events]} for organization in organizations]


    async def add_user(self, *, organization_id: int, user_id: int, permissions: str) -> Organization:


        organization = await self.db.get(Organization, organization_id)
        user = await self.db.get(User, user_id)
        link = OrganizationUserLink(organization_id=organization.id, user_id=user.id, permissions=permissions)

        self.db.add(link)
        await self.db.commit()
        await self.db.refresh(organization)

        return await self.get_organization(organization_id=organization_id)
