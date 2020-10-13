"""Blood group is 3 letters max

Revision ID: 7e9c53d0525d
Revises: 21fd69d0156a
Create Date: 2020-10-11 20:24:11.502409

"""
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "7e9c53d0525d"
down_revision = "21fd69d0156a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "user",
        "is_admin",
        existing_type=mysql.TINYINT(display_width=1),
        server_default="0",
    )
    op.alter_column(
        "donor", "blood_group", type_=mysql.VARCHAR(3), existing_nullable=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "user",
        "is_admin",
        existing_type=mysql.TINYINT(display_width=1),
        server_default=None,
    )
    op.alter_column(
        "donor", "blood_group", type_=mysql.VARCHAR(10), existing_nullable=False
    )
    # ### end Alembic commands ###