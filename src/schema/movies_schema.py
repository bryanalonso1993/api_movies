#!/usr/pipenv python3
from marshmallow import Schema, fields

class MovieSchema(Schema):
    author = fields.Str(required=True)
    description =  fields.Str(required=True)
    f_premiere = fields.Date(required=True)

