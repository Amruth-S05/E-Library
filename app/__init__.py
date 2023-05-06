from flask import Flask

from .config import Config

from .db import init_db_command


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # using config settings from config.py

    @app.route('/')
    def hello():
        return "Hello"

    app.cli.add_command(init_db_command)  # adding cli command to initialize db

    from . import auth
    app.register_blueprint(auth.admin_bp)

    return app
