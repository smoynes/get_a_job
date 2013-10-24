from flask import Flask, request, make_response
from flask.ext.restful import Api, Resource, fields, marshal_with, abort

from .models import db, Job


def configure_api(app):
    api = Api(app)
    api.add_resource(JobListResource, '/jobs', '/')
    api.add_resource(JobResource, '/jobs/<int:job_id>')
    return api

RESOURCE_FIELDS = {
    'job': {
        'status': fields.String,
        'number_one': fields.Integer(default=None),
        'number_two': fields.Integer(default=None),
        'links': fields.Raw,
    }
}


class JobResource(Resource):

    @marshal_with(RESOURCE_FIELDS)
    def get(self, job_id):
        job = Job.query.get(job_id)
        if not job:
            abort(404, message="Job {} doesn't exist".format(job_id))
        else:
            return job


class JobListResource(Resource):

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
        job = Job(number_one, number_two, status)
        db.session.add(job)
        db.session.commit()
        return job
