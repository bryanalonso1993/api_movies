#!/usr/pipenv python
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Date
from src.database.connection import db
from datetime import date

# Modelo de Peliculas
class Movies(db.Model):
    __tablename__ = "my_movies"
    id_movie: Mapped[int] = mapped_column(Integer, primary_key=True)
    author: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    f_premiere: Mapped[date] = mapped_column(Date, nullable=False)
