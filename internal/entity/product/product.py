import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.dialects import postgresql as psql

from internal.entity.base import Base
from internal.entity.product.type import ProductType


class Product(Base):

    name = sa.Column(sa.String(100), nullable=False)
    description = sa.Column(sa.Text)

    icon = sa.Column(sa.String(255))

    cost = sa.Column(sa.Float, default=0, nullable=False)

    type_id = sa.Column(
        psql.UUID(as_uuid=True),
        sa.ForeignKey('producttype.id', ondelete='CASCADE'),
        index=True,
        nullable=False,
    )

    meta = sa.Column(psql.JSONB, default=dict, nullable=False)

    type = orm.relationship(ProductType, lazy='joined')
