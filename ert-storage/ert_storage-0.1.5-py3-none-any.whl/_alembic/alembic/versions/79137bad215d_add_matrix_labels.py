"""add matrix labels

Revision ID: 79137bad215d
Revises: ba7905904381
Create Date: 2021-04-20 16:03:53.539775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "79137bad215d"
down_revision = "ba7905904381"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("f64_matrix", sa.Column("labels", sa.PickleType(), nullable=True))
    op.drop_constraint("uq_observation_name", "observation", type_="unique")
    op.create_unique_constraint(
        "uq_observation_name", "observation", ["name", "experiment_pk"]
    )
    op.create_unique_constraint("uq_update_result_pk", "update", ["ensemble_result_pk"])
    op.drop_constraint("uq_update_result_id", "update", type_="unique")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint("uq_update_result_id", "update", ["ensemble_result_pk"])
    op.drop_constraint("uq_update_result_pk", "update", type_="unique")
    op.drop_constraint("uq_observation_name", "observation", type_="unique")
    op.create_unique_constraint("uq_observation_name", "observation", ["name"])
    op.drop_column("f64_matrix", "labels")
    # ### end Alembic commands ###
