import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.dialects import postgresql as psql

from internal.entity.base import Base
from internal.entity.mixin import TimestampMixin
from internal.entity.order.status import OrderStatus
from internal.entity.product import Product
from internal.entity.user import User


class OrderProduct(Base):

    id = ...
    order_id = sa.Column(
        psql.UUID(as_uuid=True),
        sa.ForeignKey('order.id', ondelete='CASCADE'),
        index=True,
        primary_key=True,
        nullable=False,
    )
    product_id = sa.Column(
        psql.UUID(as_uuid=True),
        sa.ForeignKey('product.id', ondelete='CASCADE'),
        index=True,
        primary_key=True,
        nullable=False,
    )


class Order(TimestampMixin, Base):

    shipment_cost = sa.Column(sa.Float, default=0, nullable=False)
    shipment_at = sa.Column(sa.DateTime)

    status = sa.Column(
        psql.ENUM(OrderStatus, name='order_status'),
        default=OrderStatus.processing,
        nullable=False,
    )

    user_id = sa.Column(
        psql.UUID(as_uuid=True),
        sa.ForeignKey('user.id', ondelete='CASCADE'),
        index=True,
        nullable=False,
    )

    user = orm.relationship(User, lazy='joined')
    products = orm.relationship(
        Product, secondary=OrderProduct.__table__, lazy='joined',
    )
