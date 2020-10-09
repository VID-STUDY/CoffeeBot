"""empty message

Revision ID: 2dc47215dcb9
Revises: 47e976f22de5
Create Date: 2020-10-09 01:26:50.305370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2dc47215dcb9'
down_revision = '47e976f22de5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dishes', sa.Column('quantity', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dishes', 'quantity')
    # ### end Alembic commands ###
