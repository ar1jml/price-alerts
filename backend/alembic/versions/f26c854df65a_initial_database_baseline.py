"""initial database baseline

Revision ID: f26c854df65a
Revises: 06d1ace526b5
Create Date: 2026-09-17 20:21:30.524356

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f26c854df65a'
down_revision: Union[str, Sequence[str], None] = '06d1ace526b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
