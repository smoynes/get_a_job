from flask import Flask, request, make_response
from flask.ext.restful import Api, Resource, fields, marshal_with


app = Flask(__name__)
api = Api(app)


class Job(object):
    def __init__(self, number_one=None, number_two=None, status=None):
        self.id = 1
        self.number_one = number_one
        self.number_two = number_two
        self.status = status

    @property
    def links(self):
        links = [{'href': '/jobs', 'rel': 'index'}]
        return links


class JobListResource(Resource):
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

    def post(self):
        job = self.create_job(request)
        response = make_response('', 302)
        response.headers['Location'] = '/jobs/{}'.format(job.id)
        return response

    def create_job(self, request):
        status = request.form['job[status]']
        number_one = request.form['job[number_one]']
        number_two = request.form['job[number_two]']
        return Job(status, number_one, number_two)


api.add_resource(JobListResource, '/jobs', '/')


if __name__ == '__main__':
    app.run(debug=True)
