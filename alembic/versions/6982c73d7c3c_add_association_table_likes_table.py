"""Add association table likes_table

Revision ID: 6982c73d7c3c
Revises: 6d452b83a7d6
Create Date: 2022-02-05 13:34:16.339576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6982c73d7c3c'
down_revision = '6d452b83a7d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('association',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association')
    # ### end Alembic commands ###
