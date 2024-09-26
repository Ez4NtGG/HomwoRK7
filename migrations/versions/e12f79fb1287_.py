"""empty message

Revision ID: e12f79fb1287
Revises: 7686b2d4943e
Create Date: 2023-10-01 01:44:13.340727

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'e12f79fb1287'
down_revision: Union[str, None] = '7686b2d4943e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint('students_group_id_fkey', 'students', type_='foreignkey')
    op.create_foreign_key(None, 'students', 'groups', ['group_id'], ['id'], ondelete='SET NULL')


def downgrade() -> None:
    op.drop_constraint(None, 'students', type_='foreignkey')
    op.create_foreign_key('students_group_id_fkey', 'students', 'groups', ['group_id'], ['id'], ondelete='CASCADE')
