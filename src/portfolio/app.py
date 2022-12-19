import flask
import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker

from portfolio import validator
from portfolio.error import error_handlers


def setup_db(db_config, app):
    url = sqlalchemy.engine.url.URL.create(**db_config.to_dict())
    engine = sqlalchemy.create_engine(url)
    session_factory = sessionmaker()
    Session = scoped_session(session_factory)

    def make_session():
        return Session(bind=engine)

    app.extensions["db"] = make_session


def setup_extensions(config, app):
    app.extensions["config"] = config
    setup_db(config.database, app)


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
