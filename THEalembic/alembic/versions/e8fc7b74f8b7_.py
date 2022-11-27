"""empty message

Revision ID: e8fc7b74f8b7
Revises: fa7f7d4e4513
Create Date: 2022-11-28 00:00:46.176273

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e8fc7b74f8b7'
down_revision = 'fa7f7d4e4513'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Administrator',
    sa.Column('idAdministrator', sa.Integer(), nullable=False),
    sa.Column('FirstName', sa.String(length=25), nullable=False),
    sa.Column('LastName', sa.String(length=225), nullable=False),
    sa.Column('phone', sa.String(length=225), nullable=False),
    sa.PrimaryKeyConstraint('idAdministrator')
    )
    op.create_table('Car',
    sa.Column('idCar', sa.Integer(), nullable=False),
    sa.Column('brand', sa.String(length=225), nullable=True),
    sa.Column('model', sa.String(length=225), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('seatsNum', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=225), nullable=True),
    sa.PrimaryKeyConstraint('idCar')
    )
    op.create_table('Passenger',
    sa.Column('idPassenger', sa.Integer(), nullable=False),
    sa.Column('FirstName', sa.String(length=225), nullable=True),
    sa.Column('LastName', sa.String(length=225), nullable=True),
    sa.Column('phone', sa.String(length=225), nullable=True),
    sa.Column('documentNum', sa.String(length=225), nullable=True),
    sa.Column('address', sa.String(length=225), nullable=True),
    sa.PrimaryKeyConstraint('idPassenger')
    )
    op.create_table('RentalService',
    sa.Column('idService', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=225), nullable=True),
    sa.Column('email', sa.String(length=225), nullable=True),
    sa.Column('phone', sa.String(length=225), nullable=True),
    sa.Column('website', sa.String(length=225), nullable=True),
    sa.Column('address', sa.String(length=225), nullable=True),
    sa.PrimaryKeyConstraint('idService')
    )
    op.drop_table('car')
    op.drop_table('rentalservice')
    op.drop_table('passenger')
    op.drop_table('administrator')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('administrator',
    sa.Column('idAdministrator', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('FirstName', mysql.VARCHAR(length=25), nullable=False),
    sa.Column('LastName', mysql.VARCHAR(length=225), nullable=False),
    sa.Column('phone', mysql.VARCHAR(length=225), nullable=False),
    sa.PrimaryKeyConstraint('idAdministrator'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('passenger',
    sa.Column('idPassenger', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('FirstName', mysql.VARCHAR(length=225), nullable=True),
    sa.Column('LastName', mysql.VARCHAR(length=225), nullable=True),
    sa.Column('phone', mysql.VARCHAR(length=225), nullable=True),
    sa.Column('documentNum', mysql.VARCHAR(length=225), nullable=True),
    sa.Column('address', mysql.VARCHAR(length=225), nullable=True),
    sa.PrimaryKeyConstraint('idPassenger'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('rentalservice',
    sa.Column('idService', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=225), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=225), nullable=True),
    sa.Column('phone', mysql.VARCHAR(length=225), nullable=True),
    sa.Column('website', mysql.VARCHAR(length=225), nullable=True),
    sa.Column('address', mysql.VARCHAR(length=225), nullable=True),
    sa.PrimaryKeyConstraint('idService'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('car',
    sa.Column('idCar', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('brand', mysql.VARCHAR(length=225), nullable=True),
    sa.Column('model', mysql.VARCHAR(length=225), nullable=True),
    sa.Column('year', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('seatsNum', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('status', mysql.VARCHAR(length=225), nullable=True),
    sa.PrimaryKeyConstraint('idCar'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('RentalService')
    op.drop_table('Passenger')
    op.drop_table('Car')
    op.drop_table('Administrator')
    # ### end Alembic commands ###
