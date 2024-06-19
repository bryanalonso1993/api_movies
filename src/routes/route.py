#!/usr/pipenv python3
from src.controllers.movies_c import get_movie, create_movie, update_movie, delete_movie
from flask import Blueprint

blueprint = Blueprint('blueprint', __name__)

# root path
root_path = "/api/v1"

blueprint.route(f"{ root_path }/movie", methods=["GET"])(get_movie)
blueprint.route(f"{ root_path }/movie", methods=["POST"])(create_movie)
blueprint.route(f"{ root_path }/movie", methods=["PUT"])(update_movie)
blueprint.route(f"{ root_path }/movie", methods=["DELETE"])(delete_movie)
