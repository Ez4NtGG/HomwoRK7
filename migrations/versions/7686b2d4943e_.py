"""empty message

Revision ID: 7686b2d4943e
Revises: 9457078b93ed
Create Date: 2023-10-01 01:36:27.750985

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '7686b2d4943e'
down_revision: Union[str, None] = '9457078b93ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint('disciplines_teacher_id_fkey', 'disciplines', type_='foreignkey')
    op.create_foreign_key(None, 'disciplines', 'teachers', ['teacher_id'], ['id'], ondelete='SET NULL')


def downgrade() -> None:
    op.drop_constraint(None, 'disciplines', type_='foreignkey')
    op.create_foreign_key('disciplines_teacher_id_fkey', 'disciplines', 'teachers', ['teacher_id'], ['id'], ondelete='CASCADE')
