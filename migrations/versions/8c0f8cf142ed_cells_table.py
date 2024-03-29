"""cells table

Revision ID: 8c0f8cf142ed
Revises: 
Create Date: 2021-02-16 01:25:50.784186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c0f8cf142ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cell',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cell', sa.String(length=2), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cell_cell'), 'cell', ['cell'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cell_cell'), table_name='cell')
    op.drop_table('cell')
    # ### end Alembic commands ###
