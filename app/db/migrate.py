import os
from alembic import command
from alembic.config import Config

def run_migrations():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    alembic_ini_path = os.path.join(base_dir, "alembic.ini")

    print("Running migrations...")
    print("Alembic ini path:", alembic_ini_path)

    alembic_cfg = Config(alembic_ini_path)
    command.upgrade(alembic_cfg, "head")

    print("Migrations completed.")