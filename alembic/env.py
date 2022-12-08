from __future__ import with_statement
from alembic import context
from sqlalchemy import engine_from_config, pool
from sqlalchemy.engine.url import URL
from logging.config import fileConfig

from configly import Config

from portfolio.models import Base

config = context.config

fileConfig(config.config_file_name)

"""
Load models metadata. We should define schema in this class firstly, 
or set schema implicit with `__table_args__ = {'schema' : 'test'}` in model class
"""
target_metadata = Base.metadata


def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    config_yml = Config.from_yaml("config.yml")
    context.config.set_main_option(
        "sqlalchemy.url", str(URL.create(**config_yml.database.to_dict()))
    )
    connectable = engine_from_config(
        context.config.get_section(context.config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata, include_schemas=True
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
