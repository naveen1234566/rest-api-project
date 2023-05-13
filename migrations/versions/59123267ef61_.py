"""empty message

Revision ID: 59123267ef61
Revises: a1987b7ebf61
Create Date: 2023-05-13 11:17:44.791297

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59123267ef61'
down_revision = 'a1987b7ebf61'
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
