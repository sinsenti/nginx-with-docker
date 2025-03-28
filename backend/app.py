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

# Create tables (only needed once to create tables)
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

    # Check if user exists in the database
    user = User.query.filter_by(username=username).first()

    if user and bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
