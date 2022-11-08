# pip install Flask, Flask-Pydantic, Pydantic
from flask import Flask
from flask_pydantic import validate
from pydantic import BaseModel


class Body(BaseModel):
    first_name: str
    last_name: str
    age: int
    is_married: bool


app = Flask(__name__)


@app.route("/person", methods=["POST"])
@validate()
def create(body: Body):
    return body


app.run()