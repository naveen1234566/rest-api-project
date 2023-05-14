"""empty message

Revision ID: 38618002ac93
Revises: e48bb9d9ea7c
Create Date: 2023-05-13 22:00:59.572887

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38618002ac93'
down_revision = 'e48bb9d9ea7c'
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
