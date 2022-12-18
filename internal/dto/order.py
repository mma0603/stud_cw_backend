from datetime import datetime
from typing import Any, Dict, List
from uuid import UUID

from pydantic import BaseModel

from internal.dto.product import ProductRead
from internal.dto.user import UserRead
from internal.entity.order.status import OrderStatus


class BaseOrder(BaseModel):

    shipment_cost: float

    created_at: datetime
    shipment_at: datetime | None

    status: OrderStatus


class OrderRead(BaseOrder):

    id: UUID

    user: UserRead
    products: List[ProductRead]

    class Config(object):
        orm_mode = True


class OrderBody(BaseModel):

    products_id: List[UUID]


class OrderCreate(OrderBody):

    user_id: UUID

    @classmethod
    def from_body(cls, user_id: UUID, dto: OrderBody) -> 'OrderCreate':
        return cls(user_id=user_id, **dto.dict())


class OrderUpdate(BaseModel):

    shipment_cost: float | None
    shipment_at: datetime | None

    status: OrderStatus | None

    def dict(self, **kwargs) -> Dict[str, Any]:
        return super().dict(exclude_unset=True, **kwargs)
