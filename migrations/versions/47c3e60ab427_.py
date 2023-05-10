"""empty message

Revision ID: 47c3e60ab427
Revises: 96ec91595f2d
Create Date: 2023-05-10 09:13:53.091285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47c3e60ab427'
down_revision = '96ec91595f2d'
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
