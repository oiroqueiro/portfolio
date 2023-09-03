"""empty message

Revision ID: 4e7fcf8a60ba
Revises: 46a4e16c27c0
Create Date: 2023-09-03 16:22:38.064779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e7fcf8a60ba'
down_revision = '46a4e16c27c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('portfolio_content', schema=None) as batch_op:
        batch_op.drop_column('link')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('portfolio_content', schema=None) as batch_op:
        batch_op.add_column(sa.Column('link', sa.VARCHAR(length=150), nullable=True))

    # ### end Alembic commands ###