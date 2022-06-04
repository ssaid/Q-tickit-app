from typing import List
from sqlmodel import select
from sqlalchemy.orm import joinedload

from .base import BaseRepository
from ...models.models import *


class OrganizationRepository(BaseRepository):

    def create_organization(self, *, new_organization: OrganizationCreate) -> OrganizationRead:

        import wdb; wdb.set_trace()
        organization = Organization(**new_organization.dict())
        user = self.db.get(User, new_organization.user_id)
        organization.users = [user]

        self.db.add(organization)

        self.db.commit()
        self.db.refresh(organization)

        return organization

    def get_organization(self, *, organization_id: int) -> OrganizationRead:
        res = self.db.get(Organization, organization_id)

        if not res:
            raise HTTPException(status_code=404, detail="Organization not found")


        return res



    def get_organizations_for_user(self, user_id) -> List[Organization]:
        res = self.db.execute(select(Organization).options(
                                        joinedload(Organization.users, innerjoin=True)).filter_by(user_id=user_id)
                                    )
        organizations = res.scalars()

        return [organization.dict() for organization in organizations.unique()]

    def get_organizations(self) -> List[Organization]:

        res = self.db.execute(select(Organization).options(
                                        joinedload(Organization.users),
                                        joinedload(Organization.events))
                                    )
        organizations = res.scalars()

        return [{**organization.dict(), 'events': [event.dict() for event in organization.events]} for organization in organizations]


    def add_user(self, *, organization_id: int, user_id: int, permissions: str) -> Organization:


        organization = self.db.get(Organization, organization_id)
        user = self.db.get(User, user_id)
        link = OrganizationUserLink(organization_id=organization.id, user_id=user.id, permissions=permissions)

        self.db.add(link)
        self.db.commit()
        self.db.refresh(organization)

        return self.get_organization(organization_id=organization_id)
