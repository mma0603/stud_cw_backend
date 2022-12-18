from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends

from internal.dto.product.type import (
    ProductTypeCreate,
    ProductTypeRead,
    ProductTypeUpdate,
)
from internal.dto.user.request import RequestUser
from internal.entity.product.type import ProductType
from internal.service.product.type import ProductTypeService
from internal.usecase.utils import dependencies

router = APIRouter()


@router.get(
    path='',
    response_model=List[ProductTypeRead],
)
async def read_product_type(
    product_type_service: ProductTypeService = Depends(),
) -> List[ProductType]:
    return await product_type_service.find()


@router.post(
    path='',
    response_model=ProductTypeRead,
)
async def create_product_type(
    dto: ProductTypeCreate,
    product_type_service: ProductTypeService = Depends(),
    _: RequestUser = Depends(dependencies.get_manager_user),
) -> ProductType:
    return await product_type_service.create(dto)


@router.patch(
    path='/{product_type_id}',
    response_model=ProductTypeRead,
)
async def update_product_type(
    product_type_id: UUID,
    dto: ProductTypeUpdate,
    product_type_service: ProductTypeService = Depends(),
    _: RequestUser = Depends(dependencies.get_manager_user),
) -> ProductType:
    return await product_type_service.update(product_type_id, dto)
