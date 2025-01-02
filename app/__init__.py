""" init file for the app
We are seperating the run and app file to prevent ciruclar depedency
"""

from flask import Flask
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Initialize extensions
db = SQLAlchemy()
redis_client = FlaskRedis()


def create_app():
    """
    creating the flask server
    """
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)
    # Debug: Print the database URI
    print("Database URI:", app.config['SQLALCHEMY_DATABASE_URI'])

    # Initialize SQLAlchemy and redis with the app
    db.init_app(app)
    redis_client.init_app(app)

    # Create database tables (if they don't exist)
    with app.app_context():
        db.create_all()

    # Register blueprints or routes
    # from blueprints import doctor
    # from blueprints import patient
    # from blueprints import health_records
    # app.register_blueprint(doctor)
    # app.register_blueprint(health_records)
    # app.register_blueprint(patient)

    return app
