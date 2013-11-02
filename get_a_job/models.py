from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_one = db.Column(db.Integer)
    number_two = db.Column(db.Integer)
    answer = db.Column(db.Integer)
    status = db.Column(db.String)

    def __init__(self, number_one=None, number_two=None, status=None):
        self.number_one = number_one
        self.number_two = number_two
        self.status = status
        self.answer = None

    @property
    def links(self):
        links = [{'href': '/jobs', 'rel': 'index'}]
        return links

    def __repr__(self):
        return '<Job id=%r number_one=%r number_two=%r answer=%r status=%r>' % \
            (self.id, self.number_one, self.number_two, self.answer,
             self.status)

    def __eq__(self, other):
        if isinstance(other, Job):
            return self.number_one == other.number_one and \
                self.number_two == other.number_two and \
                self.status == other.status
        else:
            return NotImplemented

    def __ne__(self, other):
        return not self == other
