from flask import Flask
from flask.ext.restful import Api, Resource, fields, marshal_with


app = Flask(__name__)
api = Api(app)


class Job(object):
    def __init__(self, number_one=None, number_two=None, status=None):
        self.number_one = number_one
        self.number_two = number_two
        self.status = status

    @property
    def links(self):
        links = [{'href': '/jobs', 'rel': 'index'}]
        return links


class JobList(Resource):
    RESOURCE_FIELDS = {
        'job': {
            'status': fields.String,
            'number_one': fields.Integer(default=None),
            'number_two': fields.Integer(default=None),
            'links': fields.Raw,
        }
    }

    @marshal_with(RESOURCE_FIELDS)
    def get(self):
        return Job()

api.add_resource(JobList, '/', '/jobs')


if __name__ == '__main__':
    app.run(debug=True)
