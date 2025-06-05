"""empty message

Revision ID: e7455604263f
Revises: 
Create Date: 2025-06-05 10:53:07.190760

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e7455604263f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('username', sa.String, unique=True, index=True),
        sa.Column('hashed_password', sa.String)
    )

    op.create_table(
        'files',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('original_filename', sa.Text),
        sa.Column('size', sa.Integer),
        sa.Column('url', sa.Text),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'))
    )


def downgrade():
    op.drop_table('files')
    op.drop_table('users')