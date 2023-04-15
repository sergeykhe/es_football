"""Initial

Revision ID: a36c66578de3
Revises: 4aae14d87517
Create Date: 2023-04-14 18:17:58.109054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a36c66578de3'
down_revision = '4aae14d87517'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hashed_password', sa.String(), nullable=False))
    op.add_column('users', sa.Column('is_active', sa.Boolean(), nullable=False))
    op.add_column('users', sa.Column('is_superuser', sa.Boolean(), nullable=False))
    op.add_column('users', sa.Column('is_verified', sa.Boolean(), nullable=False))
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('users', 'is_verified')
    op.drop_column('users', 'is_superuser')
    op.drop_column('users', 'is_active')
    op.drop_column('users', 'hashed_password')
    # ### end Alembic commands ###