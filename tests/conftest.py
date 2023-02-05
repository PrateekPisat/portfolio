import os

import pytest
from configly import Config
from cryptography.fernet import Fernet
from flask import Flask
from pytest_mock_resources import create_postgres_fixture, PostgresConfig
from sqlalchemy.orm.session import sessionmaker

from portfolio.app import create_app
from portfolio.models import Base
from portfolio.routes import routes


@pytest.fixture(scope="session")
def pmr_postgres_config():
    return PostgresConfig(image="postgres:11-alpine")


Session = sessionmaker()

pg = create_postgres_fixture(Base, session=True)


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
            "aws": {
                "access_key_id": "FAKE_KEY",
                "secret_access_key": "FAKE_SECRET",
                "region_name": "us-east-1",
                "bucket": "test",
            },
        }
    )


@pytest.fixture()
def app(config: Config):
    app: Flask = create_app(config, routes)
    app.config.update({"TESTING": True})
    yield app


@pytest.fixture()
def client(app: Flask):
    return app.test_client()


@pytest.fixture(scope="function")
def aws_credentials():
    os.environ.pop("AWS_PROFILE", None)
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
