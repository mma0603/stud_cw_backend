from dataclasses import dataclass
from typing import Any, Dict
from uuid import UUID

from fastapi import Query
from pydantic import BaseModel

from internal.dto.product.type import ProductTypeRead


class BaseProduct(BaseModel):

    name: str
    description: str | None

    icon: str | None

    cost: float

    type: ProductTypeRead

    meta: Dict[str, Any]


class ProductRead(BaseProduct):

    id: UUID

    class Config(object):
        orm_mode = True


class ProductCreate(BaseModel):

    name: str
    description: str | None

    icon: str | None

    cost: float

    type_id: UUID

    meta: Dict[str, Any] | None


class ProductUpdate(BaseModel):

    name: str | None
    description: str | None

    icon: str | None

    cost: float | None

    type_id: UUID | None

    meta: Dict[str, Any] | None

    def dict(self, **kwargs) -> Dict[str, Any]:
        return super().dict(exclude_unset=True, **kwargs)


@dataclass
class ProductFilter(object):

    name: str = Query('')

    cost_min: float = Query(0)
    cost_max: float = Query(1000000)

    type_id: UUID | None = Query(None)
