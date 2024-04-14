"""Database creation

Revision ID: a26fb5385529
Revises: 
Create Date: 2024-04-14 00:08:11.671228

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a26fb5385529'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
            sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('name', sa.String(length=255), nullable=False),
                    sa.Column('permission', sa.JSON(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
    )
    op.create_table('users',
            sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('email', sa.String(length=255), nullable=False),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('registred_at', sa.TIMESTAMP(), nullable=True),
                    sa.Column('role_id', sa.INTEGER(), nullable=True),
                    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('roles')
    # ### end Alembic commands ###