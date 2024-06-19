#!/usr/pipenv python3
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
import os

auth = HTTPBasicAuth()

auth_api_user = {
    os.environ["USERNAME_API"] : generate_password_hash(os.environ["PASSWORD_API"])
}

@auth.verify_password
def verify_password(username, password):
    if username in auth_api_user and check_password_hash(auth_api_user.get(username), password):
        return username
