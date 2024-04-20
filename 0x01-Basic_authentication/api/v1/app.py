#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


AUTH_TYPE = getenv("AUTH_TYPE", "auth")

if AUTH_TYPE == "":
    auth = BasicAuth()
else:
    auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """
    Error handler: Unauthorized
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """
    Error handler: Forbidden
    the error handler for 403 will be executed
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def handler_before_request():
    """
    handler_before_reques
    """
    if auth is None:
        return
    excluded_paths = ['/api/v1/status/',
                      '/api/v1/unauthorized/', '/api/v1/forbidden/']
    if auth.require_auth(request.path, excluded_paths):
        if auth.authorization_header(request) is None:
            abort(401)
        if not auth.current_user(request):
            abort(403)


def _verify_credentials(request):
    """
    Extract the Authorization header value from the request
    # No Authorization header present
    # Perform authentication logic based on
    the provided credentials in the Authorization header
    # Example: You might decode the credentials and verify them against
    a database or some other source
    # If the credentials are valid,
    return True; otherwise, return False
    return False  # Placeholder implementation;
    replace with your actual authentication logic
    """
    auth_header = auth.authorization_header(request)
    if not auth_header:
        return False


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
