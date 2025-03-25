from app_factory import create_app, db
from models.user import User
from flask import request, jsonify, abort
import logging

app = create_app()

# Set up logging
logging.basicConfig(level=logging.INFO)


@app.route("/api/login", methods=["POST"])
def login():
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Missing username or password"}), 400

        user = User.query.filter_by(username=username).first()

        if user:
            return jsonify({"message": "User already exists"}), 409

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        logging.error(f"Error in login: {e}")
        abort(500, description="Internal Server Error")


@app.route("/health")
def health():
    return "Healthy", 200


if __name__ == "__main__":
    # Ensure the Flask app runs in production mode
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
