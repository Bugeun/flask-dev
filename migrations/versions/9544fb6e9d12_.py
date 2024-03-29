"""empty message

Revision ID: 9544fb6e9d12
Revises: 1fafbd1533c8
Create Date: 2024-02-07 16:12:12.711687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9544fb6e9d12'
down_revision = '1fafbd1533c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(batch_op.f('fk_question_user_id_user'), 'user', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_question_user_id_user'), type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
