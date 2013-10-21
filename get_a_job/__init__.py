from flask import Flask
from flask.ext.restful import Api

from .models import db
from .api import JobListResource


def create_app(object_name):
    app = Flask(object_name)
    app.config.from_object(object_name)
    db.init_app(app)

    api = Api(app)

    api.add_resource(JobListResource, '/jobs', '/')

    return app
