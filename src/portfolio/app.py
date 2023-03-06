import boto3
import flask
import sqlalchemy
from configly import Config
from flask import Flask
from sqlalchemy.orm import scoped_session, sessionmaker

from portfolio import validator
from portfolio.error import error_handlers


def setup_db(db_config, app):
    url = sqlalchemy.engine.url.URL.create(**db_config.to_dict())
    engine = sqlalchemy.create_engine(url)

    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)

    def make_session():
        return Session()

    app.extensions["db"] = make_session


def setup_s3(aws_config: Config, app: Flask):
    s3_client = boto3.client("s3", region_name=aws_config.region_name)
    app.extensions["s3"] = s3_client


def setup_extensions(config, app):
    app.extensions["config"] = config
    setup_db(config.database, app)
    setup_s3(config.aws, app)


def register_error_handlers(app):
    for error_cls, handler_fn in error_handlers:
        app.register_error_handler(error_cls, handler_fn)


def create_app(config, routes):
    app = flask.Flask(__name__, static_url_path="/_static")

    setup_extensions(config, app)
    register_error_handlers(app)
    validator.register(app)

    for method, path, view in routes:
        endpoint = ".".join([view.__module__, view.__name__])
        decorator = app.route(path, methods=[method], endpoint=endpoint)

        decorator(view)

    return app
