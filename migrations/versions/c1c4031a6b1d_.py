"""empty message

Revision ID: c1c4031a6b1d
Revises: 3365b5e8de69
Create Date: 2023-10-07 18:14:17.369951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1c4031a6b1d'
down_revision = '3365b5e8de69'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('portfolio_content', schema=None) as batch_op:
        batch_op.alter_column('value',
               existing_type=sa.VARCHAR(length=250),
               type_=sa.Text(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('portfolio_content', schema=None) as batch_op:
        batch_op.alter_column('value',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=250),
               existing_nullable=True)

    # ### end Alembic commands ###