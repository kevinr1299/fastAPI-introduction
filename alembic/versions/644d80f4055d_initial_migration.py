"""Initial migration

Revision ID: 644d80f4055d
Revises: 2777f22c4ddd
Create Date: 2020-10-19 11:00:16.171591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '644d80f4055d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(100), unique=True),
        sa.Column('password', sa.String(64)),
    )


def downgrade():
    op.drop_table('users')
