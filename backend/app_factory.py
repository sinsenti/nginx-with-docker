from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL", "postgresql://user:password@db:5432/mydatabase"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "mysecretkey")
    app.config["SESSION_COOKIE_SECURE"] = True  # Ensure secure cookies in production

    db.init_app(app)

    # Initialize the database when the app starts
    with app.app_context():
        from models.user import User

        db.create_all()

    return app
