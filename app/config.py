"""Configuration settings for the backend application.

This module defines the `Config` class, which holds configuration
variables such as database URIs, secret keys, and other settings.
These values can be set via environment variables or default to
sensible defaults.
"""

import os


class Config:
    """Holds configuration settings for the application.

    Attributes:
        SECRET_KEY (str): Secret key for securing the application.
            Defaults to 'your-secret-key' if not set in the environment.
        SQLALCHEMY_DATABASE_URI (str): URI for the database connection.
            Defaults to 'sqlite:///app.db' if not set in the environment.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Disables Flask-SQLAlchemy
            event tracking to save resources.
        REDIS_URL (str): URL for the Redis server.
            Defaults to 'redis://localhost:6379/0' if not set in the environment
    """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
        'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'
