from flask import Flask, request, make_response
from flask.ext.restful import Resource, fields, marshal_with

from .models import db, Job


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
        job = Job(status, number_one, number_two)
        db.session.add(job)
        db.session.commit()
        return job
