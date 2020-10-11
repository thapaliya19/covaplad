"""Initial draft for database diagram

Revision ID: 730ca38534b2
Revises: 16560cb60091
Create Date: 2020-10-11 17:37:49.073137

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "730ca38534b2"
down_revision = "16560cb60091"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "country",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "disease",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("icd_code", sa.String(length=10), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("icd_code"),
    )
    op.create_table(
        "event_type",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "province",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("country_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["country_id"],
            ["country.id"],
        ),
        sa.PrimaryKeyConstraint("id", "country_id"),
    )
    op.create_table(
        "district",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("province_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["province_id"],
            ["province.id"],
        ),
        sa.PrimaryKeyConstraint("id", "province_id"),
    )
    op.create_table(
        "city",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("district_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["district_id"],
            ["district.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "donor_disease",
        sa.Column("donor_id", sa.Integer(), nullable=False),
        sa.Column("disease_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["disease_id"],
            ["disease.id"],
        ),
        sa.ForeignKeyConstraint(
            ["donor_id"],
            ["donor.id"],
        ),
        sa.PrimaryKeyConstraint("donor_id", "disease_id"),
    )
    op.create_table(
        "skill",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("details", sa.Text(), nullable=False),
        sa.Column("volunteer_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["volunteer_id"],
            ["volunteer.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "volunteer_skills",
        sa.Column("volunteer_id", sa.Integer(), nullable=False),
        sa.Column("skill_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["skill_id"],
            ["skill.id"],
        ),
        sa.ForeignKeyConstraint(
            ["volunteer_id"],
            ["volunteer.id"],
        ),
        sa.PrimaryKeyConstraint("volunteer_id", "skill_id"),
    )
    op.add_column("donation_venue", sa.Column("city_id", sa.Integer(), nullable=False))
    op.create_foreign_key(None, "donation_venue", "city", ["city_id"], ["id"])
    op.drop_column("donation_venue", "address")
    op.add_column("donor", sa.Column("age", sa.Integer(), nullable=False))
    op.add_column(
        "donor", sa.Column("blood_group", sa.String(length=10), nullable=False)
    )
    op.add_column("donor", sa.Column("test_report", sa.Text(), nullable=True))
    op.add_column("donor", sa.Column("weight", sa.Integer(), nullable=False))
    op.add_column("event", sa.Column("city_id", sa.Integer(), nullable=False))
    op.add_column("event", sa.Column("event_type_id", sa.Integer(), nullable=False))
    op.create_foreign_key(None, "event", "city", ["city_id"], ["id"])
    op.create_foreign_key(None, "event", "event_type", ["event_type_id"], ["id"])
    op.drop_column("event", "address")
    op.drop_column("event", "name")
    op.add_column(
        "user", sa.Column("permanent_address_id", sa.Integer(), nullable=True)
    )
    op.add_column(
        "user", sa.Column("temporary_address_id", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(None, "user", "city", ["temporary_address_id"], ["id"])
    op.create_foreign_key(None, "user", "city", ["permanent_address_id"], ["id"])
    op.drop_column("user", "address")
    op.add_column(
        "volunteer",
        sa.Column("interested_fields", sa.String(length=100), nullable=False),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("volunteer", "interested_fields")
    op.add_column(
        "user", sa.Column("address", mysql.VARCHAR(length=255), nullable=True)
    )
    op.drop_constraint(None, "user", type_="foreignkey")
    op.drop_constraint(None, "user", type_="foreignkey")
    op.drop_column("user", "temporary_address_id")
    op.drop_column("user", "permanent_address_id")
    op.add_column("event", sa.Column("name", mysql.VARCHAR(length=100), nullable=False))
    op.add_column(
        "event", sa.Column("address", mysql.VARCHAR(length=255), nullable=False)
    )
    op.drop_constraint(None, "event", type_="foreignkey")
    op.drop_constraint(None, "event", type_="foreignkey")
    op.drop_column("event", "event_type_id")
    op.drop_column("event", "city_id")
    op.drop_column("donor", "weight")
    op.drop_column("donor", "test_Report")
    op.drop_column("donor", "blood_group")
    op.drop_column("donor", "age")
    op.add_column(
        "donation_venue",
        sa.Column("address", mysql.VARCHAR(length=255), nullable=False),
    )
    op.drop_constraint(None, "donation_venue", type_="foreignkey")
    op.drop_column("donation_venue", "city_id")
    op.drop_table("volunteer_skills")
    op.drop_table("skill")
    op.drop_table("donor_disease")
    op.drop_table("city")
    op.drop_table("district")
    op.drop_table("province")
    op.drop_table("event_type")
    op.drop_table("disease")
    op.drop_table("country")
    # ### end Alembic commands ###
