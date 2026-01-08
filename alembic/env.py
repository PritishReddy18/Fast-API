import sys
import os
import traceback

print("=== ALEMBIC ENV START ===")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR:", BASE_DIR)

if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)
    print("Added BASE_DIR to sys.path")

print("sys.path:", sys.path)

try:
    from logging.config import fileConfig

    from sqlalchemy import engine_from_config, pool
    from alembic import context

    from app.db.base import Base
    from app.orm_models.profile_orm_models import CreateProfile
    from app.orm_models.user_orm_models import User
    from app.orm_models.posts_orm_model import CreatePost
    from app.orm_models.post_likes import PostLikes

    # this is the Alembic Config object
    config = context.config
    database_url = os.getenv("DATA_BASE") or os.getenv("DATABASE_URL")
    if not database_url:
        raise RuntimeError("DATABASE_URL is not set for Alembic")
    config.set_main_option("sqlalchemy.url", database_url)

    # Interpret the config file for Python logging.
    if config.config_file_name is not None:
        fileConfig(config.config_file_name)

    # Set metadata
    target_metadata = Base.metadata

    # 🔥 IMPORTANT: Read DATABASE_URL from env
    DATABASE_URL = os.getenv("DATA_BASE")

    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL is not set for Alembic")

    # psycopg compatibility
    if DATABASE_URL.startswith("postgresql://"):
        DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg://", 1)

    # Inject into Alembic
    config.set_main_option("sqlalchemy.url", DATABASE_URL)


    def run_migrations_offline() -> None:
        context.configure(
            url=DATABASE_URL,
            target_metadata=target_metadata,
            literal_binds=True,
            dialect_opts={"paramstyle": "named"},
        )

        with context.begin_transaction():
            context.run_migrations()


    def run_migrations_online() -> None:
        connectable = engine_from_config(
            config.get_section(config.config_ini_section, {}),
            prefix="sqlalchemy.",
            poolclass=pool.NullPool,
        )

        with connectable.connect() as connection:
            context.configure(connection=connection, target_metadata=target_metadata)

            with context.begin_transaction():
                context.run_migrations()


    if context.is_offline_mode():
        run_migrations_offline()
    else:
        run_migrations_online()
except Exception:
    print("=== ALEMBIC ENV CRASH ===")
    traceback.print_exc()
    raise