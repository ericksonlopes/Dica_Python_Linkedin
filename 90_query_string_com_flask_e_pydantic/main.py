# pip install Flask, Flask-Pydantic, Pydantic
from typing import Optional

from flask import Flask
from pydantic import BaseModel
from flask_pydantic import validate, ValidationError


class QueryParams(BaseModel):
    first_name: Optional[str]
    is_married: Optional[bool]


app = Flask(__name__)


@app.route("/person", methods=["GET"])
@validate()
def get(query: QueryParams):
    return {"query": query.dict()}


app.run()