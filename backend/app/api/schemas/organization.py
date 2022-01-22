from pydantic import BaseModel
from typing import Optional, List
from .core import CoreModel, IDModelMixin
from .role import RoleBase



class OrganizationBase(CoreModel):
    name: str

class ClientOnOrganization(BaseModel):
    organization: OrganizationBase
    role: RoleBase

class OrganizationCreate(OrganizationBase):
    city: Optional[str] = None
    state: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    logo: Optional[str] = None
    is_active: Optional[bool] = True


class OrganizationInDB(IDModelMixin, OrganizationBase):
    pass
