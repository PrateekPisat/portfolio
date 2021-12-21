from flask import Flask
from configly import Config


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    config = Config.from_yaml("config.yaml")

    app.config.from_mapping(SECRET_KEY=config.flask.secret)

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    return app