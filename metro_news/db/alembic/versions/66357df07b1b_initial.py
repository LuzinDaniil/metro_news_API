"""Initial

Revision ID: 66357df07b1b
Revises: 
Create Date: 2021-10-10 09:24:32.260173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66357df07b1b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('news_table',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('image', sa.Text(), nullable=True),
    sa.Column('url', sa.Text(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('processing_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__news_table')),
    sa.UniqueConstraint('title', name=op.f('uq__news_table__title'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('news_table')
    # ### end Alembic commands ###