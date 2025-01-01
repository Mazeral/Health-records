""" init file for the app
We are seperating the run and app file to prevent ciruclar depedency
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis

# Initialize extensions
db = SQLAlchemy()
redis_client = FlaskRedis()


def create_app():
    """
    creating the flask server
    """
    app = Flask(__name__)

    # Load configuration
    app.config.from_pyfile('config.py')

    # Initialize extensions with the app
    db.init_app(app)
    redis_client.init_app(app)

    # Register blueprints or routes
    # from .routes import main_bp
    # app.register_blueprint(main_bp)

    return app
