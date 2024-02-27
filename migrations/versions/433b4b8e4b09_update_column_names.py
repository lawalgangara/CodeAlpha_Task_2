"""Update column names

Revision ID: 433b4b8e4b09
Revises: 
Create Date: 2024-02-22 14:07:40.670937

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '433b4b8e4b09'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('expense', schema=None) as batch_op:
        batch_op.add_column(sa.Column('amount_of_expense', sa.Integer(), nullable=False))
        batch_op.drop_column('amout_of_expense')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('expense', schema=None) as batch_op:
        batch_op.add_column(sa.Column('amout_of_expense', mysql.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_column('amount_of_expense')

    # ### end Alembic commands ###