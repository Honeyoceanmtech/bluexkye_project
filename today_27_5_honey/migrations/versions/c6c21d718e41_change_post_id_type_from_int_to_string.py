"""change post_id type from int to string

Revision ID: c6c21d718e41
Revises: 77c7dce6d4ba
Create Date: 2024-05-28 10:56:36.878505

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c6c21d718e41'
down_revision: Union[str, None] = '77c7dce6d4ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
