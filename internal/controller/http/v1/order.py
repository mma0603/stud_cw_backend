from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends

from internal.dto.order import (
    OrderBody,
    OrderCreate,
    OrderRead,
    OrderUpdate,
)
from internal.dto.user.request import RequestUser
from internal.entity.order import Order
from internal.service.order import OrderService
from internal.usecase.utils import dependencies

router = APIRouter()


@router.get(
    path='',
    response_model=List[OrderRead],
)
async def read_orders(
    order_service: OrderService = Depends(),
    request_user: RequestUser = Depends(dependencies.get_request_user),
) -> List[Order]:
    return await order_service.find(request_user)


@router.post(
    path='',
    response_model=OrderRead,
)
async def create_order(
    dto: OrderBody,
    order_service: OrderService = Depends(),
    request_user: RequestUser = Depends(dependencies.get_request_user),
) -> Order:
    return await order_service.create(
        OrderCreate.from_body(request_user.id, dto),
    )


@router.patch(
    path='/{order_id}',
    response_model=OrderRead,
)
async def update_order(
    order_id: UUID,
    dto: OrderUpdate,
    order_service: OrderService = Depends(),
    _: RequestUser = Depends(dependencies.get_manager_user),
) -> Order:
    return await order_service.update(order_id, dto)
