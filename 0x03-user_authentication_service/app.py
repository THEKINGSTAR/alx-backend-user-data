#!/usr/bin/env python3
"""

"""


from db import DB
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
def post_users(email: str, password: str):
    """
    Define a users function
    that
    implements the POST /users route.
    
    the end-point should register it
    and
    respond with the following JSON payload:
    {"email": "<registered email>", "message": "user created"}
    
    If the user is already registered, catch the exception
    and
    return a JSON payload of the form
    {"message": "email already registered"}
    """
    email = request.json.get('email')
    password = request.json.get('password')
    if not email or not password:
        return jsonify({"message": "email and password is required"})

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": "{email}", "message": "user created"})
    except ValueError:
            return jsonify({"message": "email already registered"})
            
            

    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
