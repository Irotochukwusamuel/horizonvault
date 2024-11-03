"""add investment model

Revision ID: ab37075b779f
Revises: 722f8b2a26b4
Create Date: 2024-11-01 12:49:13.944178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab37075b779f'
down_revision = '722f8b2a26b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('investment_scheme',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('rate', sa.Float(), nullable=False),
    sa.Column('minimum', sa.Float(), nullable=False),
    sa.Column('maximum', sa.Float(), nullable=False),
    sa.Column('interval', sa.Enum('DAILY', 'MONTHLY', 'BIWEEKLY', 'WEEKLY', 'YEARLY', 'TRIDAYS', 'BIDAYS', name='investmentinterval'), nullable=False),
    sa.Column('created_at', sa.BigInteger(), nullable=True),
    sa.Column('last_updated', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('investment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('scheme_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('wallet_id', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('status', sa.Enum('PENDING', 'PROCESSING', 'APPROVED', 'FAILED', 'COMPLETED', name='investmentstatus'), nullable=False),
    sa.Column('deposit_type', sa.Enum('CASH', 'WALLET', name='deposittype'), nullable=False),
    sa.Column('created_at', sa.BigInteger(), nullable=True),
    sa.Column('last_updated', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['scheme_id'], ['investment_scheme.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['wallet_id'], ['wallet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_investment_scheme_id'), 'investment', ['scheme_id'], unique=False)
    op.create_index(op.f('ix_investment_user_id'), 'investment', ['user_id'], unique=False)
    op.create_index(op.f('ix_investment_wallet_id'), 'investment', ['wallet_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_investment_wallet_id'), table_name='investment')
    op.drop_index(op.f('ix_investment_user_id'), table_name='investment')
    op.drop_index(op.f('ix_investment_scheme_id'), table_name='investment')
    op.drop_table('investment')
    op.drop_table('investment_scheme')
    # ### end Alembic commands ###