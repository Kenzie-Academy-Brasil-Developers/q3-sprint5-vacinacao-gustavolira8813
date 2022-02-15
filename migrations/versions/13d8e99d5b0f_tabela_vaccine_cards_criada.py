"""tabela vaccine_cards criada

Revision ID: 13d8e99d5b0f
Revises: 
Create Date: 2022-02-15 00:14:12.377110

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13d8e99d5b0f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vaccine_cards',
    sa.Column('cpf', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('first_shot_date', sa.Date(), nullable=True),
    sa.Column('second_shot_date', sa.Date(), nullable=True),
    sa.Column('vaccine_name', sa.String(), nullable=False),
    sa.Column('health_unit_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('cpf')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vaccine_cards')
    # ### end Alembic commands ###
