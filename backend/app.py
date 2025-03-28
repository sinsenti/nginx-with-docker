from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from database import db, User
import os

app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL", "postgresql://user:password@db:5432/app_db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize database
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return "Flask Backend is running!"


@app.route("/api/status")
def status():
    return jsonify({"status": "Backend is running", "version": "1.0"})


@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User data stored successfully!"}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
