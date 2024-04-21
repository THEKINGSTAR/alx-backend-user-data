#!/usr/bin/env python3
""" Main 4
"""
from api.v1.auth.basic_auth import BasicAuth

a = BasicAuth()

print(a.extract_user_credentials(None))
print(a.extract_user_credentials(89))
print(a.extract_user_credentials("Holberton School"))
print(a.extract_user_credentials("Holberton:School"))
print(a.extract_user_credentials("bob@gmail.com:toto1234"))

"""
bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_4.py
(None, None)
(None, None)
(None, None)
('Holberton', 'School')
('bob@gmail.com', 'toto1234')
bob@dylan:~$
"""
