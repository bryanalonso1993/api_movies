#!/usr/pipenv python3
from flask import Flask
import os

# Base de datos
from src.database.connection import db

# Rutas
from src.routes.route import blueprint

app = Flask(__name__)

# App config
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["SQLALCHEMY_DATABASE_URI"]

# Activo el modo debug para validar las consultas ejecutadas por el ORM, en prod desactivar
app.config['SQLALCHEMY_ECHO'] = True

app.register_blueprint(blueprint, url_prefix="/")

# initialize the app with the extension
try:
    db.init_app(app)
    with app.app_context():
        db.create_all()
except Exception as err:
    print(f"Error { err }")

# Run app
if __name__ == "__main__":
    app.run(port=7070, host="0.0.0.0", debug=True)
