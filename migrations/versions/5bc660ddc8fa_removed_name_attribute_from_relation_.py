"""Removed name attribute from relation ward

Revision ID: 5bc660ddc8fa
Revises: bc5cd64da6ab
Create Date: 2020-10-13 22:43:07.499485

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "5bc660ddc8fa"
down_revision = "bc5cd64da6ab"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("ward", "name")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("ward", sa.Column("name", mysql.VARCHAR(length=100), nullable=True))
    # ### end Alembic commands ###