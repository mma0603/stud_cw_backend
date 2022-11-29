from typing import Dict, Any
from uuid import UUID

from pydantic import BaseModel


class BaseProductType(BaseModel):

    name: str
    description: str | None

    icon: str | None


class ProductTypeRead(BaseProductType):

    id: UUID

    class Config(object):
        orm_mode = True


class ProductTypeCreate(BaseProductType):
    pass


class ProductTypeUpdate(BaseModel):

    name: str | None
    description: str | None

    icon: str | None

    def dict(self, **kwargs) -> Dict[str, Any]:
        return super().dict(exclude_unset=True, **kwargs)
