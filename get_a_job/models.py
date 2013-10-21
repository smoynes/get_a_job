from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_one = db.Column(db.Integer)
    number_two = db.Column(db.Integer)
    status = db.Column(db.String)

    def __init__(self, number_one=None, number_two=None, status=None):
        self.number_one = number_one
        self.number_two = number_two
        self.status = status

    @property
    def links(self):
        links = [{'href': '/jobs', 'rel': 'index'}]
        return links
