"""Post model adding

Revision ID: 11c9a8998e30
Revises: 9352ee05af5e
Create Date: 2021-12-22 20:57:22.063652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11c9a8998e30'
down_revision = '9352ee05af5e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('time_created', sa.DateTime(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    # ### end Alembic commands ###
