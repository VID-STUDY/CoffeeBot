"""empty message

Revision ID: 47e976f22de5
Revises: 5b03269b927b
Create Date: 2020-10-06 22:36:54.046471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47e976f22de5'
down_revision = '5b03269b927b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('count_orders', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'count_orders')
    # ### end Alembic commands ###
