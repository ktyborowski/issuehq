from flask import Blueprint, Flask
from issuehq.db import db
from flask_cors import CORS
from flask import json
from werkzeug.exceptions import HTTPException
from issuehq.collections import create_collections
from huey import SqliteHuey
from issuehq.collections import wclient


app = Flask("IssueHQ")

CORS(app)

huey = SqliteHuey("issuehq", filename="huey.db")

wclient.connect()
create_collections()


@app.before_request
def before_request():
    if db.is_closed():
        db.connect()


@app.after_request
def after_request(response):
    if not db.is_closed():
        db.close()

    return response


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return HTTP errors as JSON."""

    response = e.get_response()
    response.data = json.dumps(
        {
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }
    )
    response.content_type = "application/json"
    return response


root = Blueprint("root", __name__)
app.register_blueprint(root, url_prefix="/")
