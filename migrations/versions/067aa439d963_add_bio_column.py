"""add bio column

Revision ID: 067aa439d963
Revises: 61bbc954a27e
Create Date: 2020-07-22 16:25:05.790572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '067aa439d963'
down_revision = '61bbc954a27e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###