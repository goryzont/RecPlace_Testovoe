"""upgrade table request2

Revision ID: 2c1387b09bfa
Revises: 5afddfc6ecde
Create Date: 2023-11-28 16:48:47.206986

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '2c1387b09bfa'
down_revision: Union[str, None] = '5afddfc6ecde'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('requests', sa.Column('id_owner_request', sa.Integer(), nullable=False))
    op.drop_constraint('requests_owner_request_fkey', 'requests', type_='foreignkey')
    op.create_foreign_key(None, 'requests', 'users', ['id_owner_request'], ['id'])
    op.drop_column('requests', 'owner_request')
    op.add_column('users', sa.Column('request', sa.JSON(), nullable=True))
    op.drop_column('users', 'last_three_request')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('last_three_request', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
    op.drop_column('users', 'request')
    op.add_column('requests', sa.Column('owner_request', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'requests', type_='foreignkey')
    op.create_foreign_key('requests_owner_request_fkey', 'requests', 'users', ['owner_request'], ['id'])
    op.drop_column('requests', 'id_owner_request')
    # ### end Alembic commands ###
