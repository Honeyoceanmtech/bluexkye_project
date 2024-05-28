"""rename content to post_content in post

Revision ID: 63b25353c431
Revises: cf24c942afaa
Create Date: 2024-05-28 10:47:01.194655

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '63b25353c431'
down_revision: Union[str, None] = 'cf24c942afaa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
