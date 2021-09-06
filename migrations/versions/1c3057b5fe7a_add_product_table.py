"""Add product table

Revision ID: 1c3057b5fe7a
Revises: 
Create Date: 2021-09-06 11:08:14.790829

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c3057b5fe7a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('product',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('price', sa.Float(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_id'), 'product', ['id'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_product_id'), table_name='product')
    op.drop_table('product')
