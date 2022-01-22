from pydantic import BaseModel
from typing import Optional
from .core import CoreModel, IDModelMixin


class RoleBase(CoreModel):
    name: str

class RoleInDB(IDModelMixin, RoleBase):
    pass


class RoleCreate(RoleBase):
    pass

