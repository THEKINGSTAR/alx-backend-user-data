#!/usr/bin/env python3
"""

"""


from db import DB
from user import User, Base
from sqlalchemy.orm.exc import NoResultFound
from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route('/')
def single_GET():
    """

    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
