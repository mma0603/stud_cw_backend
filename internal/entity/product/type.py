import sqlalchemy as sa

from internal.entity.base import Base


class ProductType(Base):

    __table_args__ = (
        sa.UniqueConstraint('name'),
    )

    name = sa.Column(sa.String(100), nullable=False)
    description = sa.Column(sa.Text)

    icon = sa.Column(sa.String(255))
