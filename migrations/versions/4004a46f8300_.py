"""empty message

Revision ID: 4004a46f8300
Revises: 631eb1348410
Create Date: 2023-05-13 13:08:51.849979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4004a46f8300'
down_revision = '631eb1348410'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###
