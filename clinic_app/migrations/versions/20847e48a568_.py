"""empty message

Revision ID: 20847e48a568
Revises: e0a8bcac6604
Create Date: 2021-12-13 23:10:23.800685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20847e48a568'
down_revision = 'e0a8bcac6604'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appointment', sa.Column('last_update', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True))
    op.add_column('patient', sa.Column('last_update', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True))
    op.add_column('user', sa.Column('last_update', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_update')
    op.drop_column('patient', 'last_update')
    op.drop_column('appointment', 'last_update')
    # ### end Alembic commands ###
