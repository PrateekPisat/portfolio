# flake8: noqa
import logging

from configly import Config

from portfolio.app import create_app
from portfolio.routes import routes
from setuplog import setup_logging

config = Config.from_yaml("config.yml")
setup_logging(config.logging.level)
app = create_app(config, routes)


if __name__ == "__main__":
    app.run(**{opt: val for opt, val in config.flask if val is not None})
