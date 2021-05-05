"""Add analyzer commands for reports

Revision ID: c88f85da2a06
Revises: af5d8a21c1e4
Create Date: 2021-05-05 09:22:53.624635

"""

# revision identifiers, used by Alembic.
revision = 'c88f85da2a06'
down_revision = 'af5d8a21c1e4'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('analyzer_commands',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('command', sa.Binary(), nullable=True),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_analyzer_commands'))
    )

    op.create_table('report_analyzer_commands',
        sa.Column('report_id', sa.Integer(), nullable=True),
        sa.Column('analyzer_command_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['analyzer_command_id'],
            ['analyzer_commands.id'],
            name=op.f('fk_report_analyzer_commands_analyzer_command_id_analyzer_commands')),
        sa.ForeignKeyConstraint(
            ['report_id'],
            ['reports.id'],
            name=op.f('fk_report_analyzer_commands_report_id_reports'))
    )


def downgrade():
    op.drop_table('report_analyzer_commands')
    op.drop_table('analyzer_commands')
