"""empty message

Revision ID: 82dd40ac96d3
Revises: 5950cf1737dc
Create Date: 2020-06-05 19:51:21.403570

"""
from alembic import op
import sqlalchemy as sa

# here
# revision identifiers, used by Alembic.
revision = '82dd40ac96d3'
down_revision = '5950cf1737dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('actors')
    op.drop_table('movies')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('release_date', sa.VARCHAR(length=4), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='movies_pkey')
    )
    op.create_table('actors',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=25), autoincrement=False, nullable=False),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('gender', sa.VARCHAR(length=10), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='actors_pkey')
    )
    # ### end Alembic commands ###
