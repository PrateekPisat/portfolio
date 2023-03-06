from configly import Config
from setuplog import setup_logging

from portfolio.app import create_app
from portfolio.routes import routes

config = Config.from_yaml("config.yml")
setup_logging(config.logging.level)
app = create_app(config, routes)


@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
    return response


if __name__ == "__main__":
    app.run(**{opt: val for opt, val in config.flask if val is not None})
