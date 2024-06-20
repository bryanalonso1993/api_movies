#!/usr/pipenv python3
from src.database.my_movies_model import Movies
from src.database.connection import db
# Validacion de esquemas
from src.schema.movies_schema import MovieSchema
from marshmallow import ValidationError
from flask import jsonify, request

def get_movie_s():
    _id = request.args.get('id')
    container_response = []
    # Si no existe el id que traiga todos los registros
    if not _id:
        movies = db.session.execute(db.select(Movies.id_movie, Movies.author, 
                                              Movies.description, Movies.f_premiere)).fetchall()
    else:
        movies = db.session.execute(db.select(Movies.id_movie, Movies.author, 
                                              Movies.description, Movies.f_premiere)
                                              .where(Movies.id_movie == _id)).fetchall()
    container_response = [{
        'id_movie': id_movie,
        'author': author,
        'description': description,
        'f_premiere': f_premiere
    } for id_movie, author, description, f_premiere in movies]
    return jsonify({
        'data': container_response,
        'messageResponse': 'se ejecuto con exito la consulta'
    }), 200

def create_movie_s():
    req = request.json
    try:
        # Validar array de datos https://marshmallow.readthedocs.io/en/stable/quickstart.html
        MovieSchema(many=True).load(req)
    except ValidationError as err:
        return jsonify({ 'error': err.messages }), 400
    try:
        for row in req:
            movie = Movies(author=row['author'], description=row['description'], f_premiere=row['f_premiere'])
            db.session.add(movie)
        db.session.commit()
    except Exception as err:
        return jsonify({ 'error': f'Excepcion controlada { err }'})
    return jsonify({
        'data': f'Se creo el registro pelicula { row['description'] }',
        'messageResponse': 'Se creo con exito los registros'
    }), 200

# Actualizacion basada en id
def update_movie_s():
    _id = request.args.get('id')
    req = request.json
    try:
        movie_id = db.session.execute(db.update(Movies).where(Movies.id_movie == _id), req)
        db.session.commit()
        return jsonify({
            'data': f'Se actualizo el registro con id={ _id }'
        }), 200
    except Exception as err:
        return jsonify({
            'data': f'Error al actualizar el registro { err }'
        }), 404

def delete_movie_s():
    _id = request.args.get('id')
    try:
        delete_user = db.session.get(Movies, _id)
        db.session.delete(delete_user)
        db.session.commit()
        return "delete user"
    except Exception as err:
        return jsonify({
            'error': f'Error al eliminar registro: { err }'
        }), 404
