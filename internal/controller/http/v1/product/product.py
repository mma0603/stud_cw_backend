from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends

from internal.entity.product import Product
from internal.dto.product import ProductRead, ProductCreate, ProductUpdate
from internal.dto.user.request import RequestUser
from internal.service.product import ProductService
from internal.usecase.utils import (
    dependencies,
)

router = APIRouter()


@router.get(
    path='',
    response_model=List[ProductRead],
)
async def read_product(
    product_service: ProductService = Depends(),
) -> List[Product]:
    return await product_service.find()


@router.post(
    path='',
    response_model=ProductRead,
)
async def create_product(
    dto: ProductCreate,
    product_service: ProductService = Depends(),
    _: RequestUser = Depends(dependencies.get_manager_user),
) -> Product:
    return await product_service.create(dto)


@router.patch(
    path='/{product_id}',
    response_model=ProductRead,
)
async def update_product(
    product_type_id: UUID,
    dto: ProductUpdate,
    product_service: ProductService = Depends(),
    _: RequestUser = Depends(dependencies.get_manager_user),
) -> Product:
    return await product_service.update(product_type_id, dto)
