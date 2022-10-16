import sqlalchemy as sa
from sqlalchemy.dialects import postgresql as psql

from internal.entity.base import Base
from internal.entity.mixin import TimestampMixin
from internal.entity.role import Role


class User(TimestampMixin, Base):

    __table_args__ = (
        sa.UniqueConstraint('username'),
        sa.UniqueConstraint('email'),
    )

    username = sa.Column(sa.String(50), nullable=False)
    password = sa.Column(sa.String(64), nullable=False)
    email = sa.Column(sa.String(100), nullable=False)

    role = sa.Column(
        psql.ENUM(Role, name='role'), default=Role.user, nullable=False,
    )

    first_name = sa.Column(sa.String(50))
    last_name = sa.Column(sa.String(50))

    address = sa.Column(sa.String(255))
