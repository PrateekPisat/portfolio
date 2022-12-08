import flask
import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker

from app import validator


def setup_db(db_config, app):
    url = sqlalchemy.engine.url.URL.create(**db_config.to_dict())
    engine = sqlalchemy.create_engine(url)
    session_factory = sessionmaker()
    Session = scoped_session(session_factory)

    @app.teardown_appcontext
    def shutdown_session(response_or_exc):
        """Ensure that the session is removed on app context teardown."""
        Session.remove()
        return response_or_exc

    def make_session():
        return Session(bind=engine)

    app.extensions["db"] = make_session


def create_app(config, routes):
    app = flask.Flask(__name__, static_url_path="/_static")
    setup_db(config.database, app)
    validator.register(app)

    for method, path, view, required_permissions in routes:
        endpoint = ".".join([view.__module__, view.__name__])
        decorator = app.route(path, methods=[method], endpoint=endpoint)
        view = apply_route_auth(view, required_permissions, config.auth0)

        # performs the `app.route` call which ultimately registers the route with flask.
        decorator(view)

    return app
