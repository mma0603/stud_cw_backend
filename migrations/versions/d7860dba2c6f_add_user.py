"""add_user

Revision ID: d7860dba2c6f
Revises: 6406de4e4833
Create Date: 2022-10-16 18:20:10.230546

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd7860dba2c6f'
down_revision = '6406de4e4833'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.FetchedValue(), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('role', postgresql.ENUM('user', 'manager', name='role', create_type=False), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###