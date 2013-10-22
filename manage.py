import os

from flask.ext.script import Manager

from get_a_job import create_app, db


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
                          os.path.dirname(
                              os.path.abspath(__file__)) + '/dev.db'

manager = Manager(lambda: create_app(__name__))


@manager.command
def create_db():
    "Creates database schema."
    db.create_all()

if __name__ == '__main__':
    manager.run()
