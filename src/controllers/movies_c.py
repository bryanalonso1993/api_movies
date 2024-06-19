#!/usr/pipenv python3
from src.services.movies_s import get_movie_s, create_movie_s, update_movie_s, delete_movie_s
from src.auth.auth import auth

@auth.login_required
def get_movie():
    return get_movie_s()

@auth.login_required
def create_movie():
    return create_movie_s()

@auth.login_required
def update_movie():
    return update_movie_s()

@auth.login_required
def delete_movie():
    return delete_movie_s()
