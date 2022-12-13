from fastapi import APIRouter

from . import user
from .product import product, type

router = APIRouter()
router.include_router(
    user.router,
    prefix='/user',
    tags=['user'],
)
router.include_router(
    product.router,
    prefix='/product',
    tags=['product'],
)
router.include_router(
    type.router,
    prefix='/product/type',
    tags=['product_type'],
)

