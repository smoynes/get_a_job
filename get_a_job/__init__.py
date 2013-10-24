from flask import Flask
from flask.ext.restful import Api

from .models import db
from .api import configure_api

def create_app(object_name, **kwargs):
    app = Flask(object_name)
    app.config.from_object(object_name)
    app.config.update(kwargs)

    db.init_app(app)
    configure_api(app)

    return app
