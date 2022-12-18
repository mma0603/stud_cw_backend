from fastapi import APIRouter

from . import feedback, order, user
from .product import product, type

router = APIRouter()
router.include_router(
    user.router,
    prefix='/user',
    tags=['user'],
)
router.include_router(
    order.router,
    prefix='/order',
    tags=['order'],
)
router.include_router(
    feedback.router,
    prefix='/feedback',
    tags=['feedback'],
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
