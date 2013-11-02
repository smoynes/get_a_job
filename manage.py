import os

from flask.ext.script import Manager

from get_a_job import create_app, create_celery, db


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
                          os.path.dirname(
                              os.path.abspath(__file__)) + '/dev.db'
import get_a_job.tasks
app = create_app(__name__)
celery = create_celery(app)
manager = Manager(lambda: app)

@manager.command
def create_db():
    "Creates database schema."
    db.create_all()

@manager.command
def worker():
    with app.app_context():
        celery.start()

if __name__ == '__main__':
    manager.run()
