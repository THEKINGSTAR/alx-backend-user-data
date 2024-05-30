#!/usr/bin/env python3
"""

"""


from user import User, Base
from sqlalchemy.orm.exc import NoResultFound
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/')
def single_GET():
    """
    use flask.jsonify to
    return a JSON payload of the form:
    {"message": "Bienvenue"}
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def post_users():
    """
    a users function that
    implements the POST /users route.
    the end-point should register it and
    respond with the following JSON payload:
    {"email": "<registered email>", "message": "user created"}
    If the user is already registered,
    catch the exception and
    return a JSON payload of the form
    {"message": "email already registered"}
    """
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            return jsonify({"message": "email and password are required"}), 400

        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})

    except ValueError:
        return jsonify({"message": "email already registered"}), 400
# @app.route('/users', methods=['GET'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
