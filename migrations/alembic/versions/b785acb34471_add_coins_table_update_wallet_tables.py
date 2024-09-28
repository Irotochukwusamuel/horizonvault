"""add coins table & update wallet tables

Revision ID: b785acb34471
Revises: 73915ee085e7
Create Date: 2024-09-24 12:21:42.796191

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b785acb34471'
down_revision = '73915ee085e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_table('coins',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('name', sa.Text(), nullable=True),
    # sa.Column('symbol', sa.Text(), nullable=True),
    # sa.Column('logo', sa.Text(), nullable=True),
    # sa.Column('created_at', sa.BigInteger(), nullable=True),
    # sa.Column('last_updated', sa.BigInteger(), nullable=True),
    # sa.PrimaryKeyConstraint('id'),
    # sa.UniqueConstraint('logo'),
    # sa.UniqueConstraint('name'),
    # sa.UniqueConstraint('symbol')
    # )
    # op.create_foreign_key(None, 'wallet', 'coins', ['wallet_name'], ['name'])
    # op.drop_column('wallet', 'wallet_symbol')
    # op.drop_column('wallet', 'wallet_type')
    pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('wallet', sa.Column('wallet_type', mysql.VARCHAR(length=350), nullable=True))
    op.add_column('wallet', sa.Column('wallet_symbol', mysql.TEXT(), nullable=True))
    op.drop_constraint(None, 'wallet', type_='foreignkey')
    op.drop_table('coins')
    # ### end Alembic commands ###