"""change comment_views type from float to timestamp

Revision ID: 77c7dce6d4ba
Revises: 63b25353c431
Create Date: 2024-05-28 10:53:16.369737

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '77c7dce6d4ba'
down_revision: Union[str, None] = '63b25353c431'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
