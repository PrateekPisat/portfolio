import configly
import pytest
from configly import Config
from cryptography.fernet import Fernet
from pytest_mock_resources import create_postgres_fixture, PostgresConfig
from sqlalchemy.orm.session import sessionmaker

from portfolio.models import Base


@pytest.fixture(scope="session")
def pmr_postgres_config():
    return PostgresConfig(image="postgres:11-alpine")


Session = sessionmaker()

pg = create_postgres_fixture(
    Base,
    session=True,
    engine_kwargs=dict(execution_options={"schema_translate_map": {None: "public"}}),
)


@pytest.fixture
def config(pg):
    pmr_credentials = pg.connection().engine.pmr_credentials
    return Config(
        {
            "environment": "test",
            "database": {
                "drivername": pmr_credentials.drivername,
                "host": pmr_credentials.host,
                "port": pmr_credentials.port,
                "database": pmr_credentials.database,
                "username": pmr_credentials.username,
                "password": pmr_credentials.password,
            },
            "logging": {"level": "DEBUG"},
            "cryptography": {"key": Fernet.generate_key()},
        }
    )
