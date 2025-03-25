from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()  # Initialize db here


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL", "postgresql://user:password@db:5432/mydatabase"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)  # Bind db to app

    with app.app_context():
        from models.user import User  # Import models inside function

        db.create_all()

    return app
