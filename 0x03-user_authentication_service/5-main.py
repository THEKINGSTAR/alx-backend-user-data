#!/usr/bin/env python3
"""
Main file
"""


from auth import Auth


email = 'me@me.com'
password = 'mySecuredPwd'

auth = Auth()

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err))

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err))

"""
bob@dylan: ~$ python3 main.py
successfully created a new user!
could not create a new user: User me@me.com already exists
bob@dylan: ~$
"""