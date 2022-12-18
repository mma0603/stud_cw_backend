from typing import List
from uuid import UUID

from fastapi import Depends
from pytorm.repository import InjectRepository
from sqlalchemy.ext.asyncio import AsyncSession

from internal.dto.order import OrderCreate, OrderUpdate
from internal.dto.user.request import RequestUser
from internal.entity.order import Order, OrderProduct
from internal.usecase.utils import get_session


class OrderService(object):  # noqa: WPS214

    def __init__(
        self, session: AsyncSession = Depends(get_session),
    ) -> None:
        self.session = session
        self.repository = InjectRepository(Order, session)

    async def find(self, request_user: RequestUser, **attrs) -> List[Order]:
        where = set()
        if not request_user.is_manager:
            where.add(Order.user_id == request_user.id)

        return await self.repository.find(*where, **attrs)

    async def create(self, dto: OrderCreate) -> Order:
        order = self.repository.create(**dto.dict(exclude={'products_id'}))
        order = await self.repository.save(order)
        order_products = [
            OrderProduct(order_id=order.id, product_id=product_id)
            for product_id in dto.products_id
        ]
        self.session.add_all(order_products)
        await self.session.commit()
        return await self.repository.find_one(id=order.id)

    async def update(self, order_id: UUID, dto: OrderUpdate) -> Order:
        order = self.repository.create(id=order_id, **dto.dict())
        await self.repository.save(order)
        return await self.repository.find_one(id=order_id)
