"""drop comment_content column from comment

Revision ID: cf24c942afaa
Revises: f5e625fbad5e
Create Date: 2024-05-28 10:44:33.418144

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cf24c942afaa'
down_revision: Union[str, None] = 'f5e625fbad5e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
