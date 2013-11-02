from __future__ import absolute_import

from flask import Flask
from flask.ext.restful import Api
from celery import Celery

from .models import db
from .api import configure_api

def create_app(object_name, **kwargs):
    app = Flask(object_name)
    app.config.from_object(object_name)
    app.config.update(kwargs)

    db.init_app(app)
    create_api(app)
    create_celery(app)

    return app

def create_api(app):
    api = Api(app)
    configure_api(api)

def create_celery(app=None):
    app = app or create_app(__name__)
    broker = app.config.get('CELERY_BROKER_URL') or 'redis://localhost/'
    celery = Celery(broker=broker)
    celery.conf.update(app.config)

    TaskBase = celery.Task

    class ContextBase(TaskBase):
        abstract = True

        def __call__(*args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(*args, **kwargs)

    celery.Task = ContextBase
    return celery

celery = create_celery()
