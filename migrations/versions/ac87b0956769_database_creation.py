"""Database creation

Revision ID: ac87b0956769
Revises: 
Create Date: 2023-12-07 01:51:17.394707

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac87b0956769'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('decks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('size', sa.Float(precision=4, asdecimal=2), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('price', sa.Float(precision=10, asdecimal=2), nullable=True),
    sa.Column('color', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_decks_color'), 'decks', ['color'], unique=False)
    op.create_index(op.f('ix_decks_description'), 'decks', ['description'], unique=False)
    op.create_index(op.f('ix_decks_id'), 'decks', ['id'], unique=False)
    op.create_index(op.f('ix_decks_price'), 'decks', ['price'], unique=False)
    op.create_index(op.f('ix_decks_size'), 'decks', ['size'], unique=False)
    op.create_index(op.f('ix_decks_title'), 'decks', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_decks_title'), table_name='decks')
    op.drop_index(op.f('ix_decks_size'), table_name='decks')
    op.drop_index(op.f('ix_decks_price'), table_name='decks')
    op.drop_index(op.f('ix_decks_id'), table_name='decks')
    op.drop_index(op.f('ix_decks_description'), table_name='decks')
    op.drop_index(op.f('ix_decks_color'), table_name='decks')
    op.drop_table('decks')
    # ### end Alembic commands ###
