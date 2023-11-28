"""upgrade table request3

Revision ID: 6c98362c7567
Revises: 2c1387b09bfa
Create Date: 2023-11-28 16:49:59.876040

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '6c98362c7567'
down_revision: Union[str, None] = '2c1387b09bfa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('requests', sa.JSON(), nullable=True))
    op.drop_column('users', 'request')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('request', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
    op.drop_column('users', 'requests')
    # ### end Alembic commands ###