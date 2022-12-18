import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.dialects import postgresql as psql

from internal.entity.base import Base
from internal.entity.mixin import TimestampMixin
from internal.entity.user import User


class Feedback(TimestampMixin, Base):

    __table_args__ = (
        sa.CheckConstraint('mark >= 1 AND mark <= 5', name='mark_check'),
    )

    text = sa.Column(sa.Text)
    mark = sa.Column(sa.Integer, nullable=False)

    user_id = sa.Column(
        psql.UUID(as_uuid=True),
        sa.ForeignKey('user.id', ondelete='CASCADE'),
        index=True,
        nullable=False,
    )
    product_id = sa.Column(
        psql.UUID(as_uuid=True),
        sa.ForeignKey('product.id', ondelete='CASCADE'),
        index=True,
        nullable=False,
    )

    user = orm.relationship(User, lazy='joined')
