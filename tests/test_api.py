import json
import os
import tempfile
import unittest

from get_a_job import create_app
from get_a_job.models import db, Job


class TestCase(unittest.TestCase):

    def setUp(self):
        self.temp_db_fd, self.temp_db_file = tempfile.mkstemp(suffix='.db')
        config = {'SQLALCHEMY_DATABASE_URI': 'sqlite:///' + self.temp_db_file}
        app = create_app(__name__, **config)
        db.app = app
        db.create_all()
        self.app = app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        os.remove(self.temp_db_file)
        os.close(self.temp_db_fd)

    def deserialize(self, response):
        return json.loads(response)

    def assert_redirected(self, response, location):
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.headers.get('Location'), location)

    def assert_persisted(self, id, job):
        persisted_job = Job.query.get(id)
        self.assertEquals(persisted_job, job)

    def assert_response_ok(self, response):
        self.assertEquals(response.status_code, 200)

    def assert_response_not_found(self, response):
        self.assertEquals(response.status_code, 404)

    def create_job(self, number_one, number_two, status):
        job = Job(number_one, number_two, status)
        db.session.add(job)
        db.session.commit()
        return job


class JobListTestCase(TestCase):

    def test_get_index(self):
        response = self.app.get('/')
        self.assert_response_ok(response)
        empty_job = {
            "job": {
                "number_one": None,
                "number_two": None,
                "status": None,
                "links": [
                    {"href": "/jobs", "rel": "index"}
                ]
            }
        }
        job = self.deserialize(response.data)
        self.assertEquals(job, empty_job)

    def test_post_job(self):
        job = {
            'job[status]': 'in_progress',
            'job[number_one]': 1,
            'job[number_two]': 2
        }
        response = self.app.post('/jobs', data=job)
        self.assert_redirected(response, 'http://localhost/jobs/1')
        self.assert_persisted(id=1, job=Job(1, 2, 'in_progress'))


class JobTestCase(TestCase):

    def test_get(self):
        existing_job = self.create_job(
            number_one=2,
            number_two=3,
            status='in_progress')
        response = self.app.get('/jobs/{}'.format(existing_job.id))
        expected_job = {
            "job": {
                "number_one": 2,
                "number_two": 3,
                "status": 'in_progress',
                "links": [
                    {"href": "/jobs", "rel": "index"}
                ]
            }
        }
        self.assert_response_ok(response)
        job = self.deserialize(response.data)
        self.assertEquals(job, expected_job)

    def test_get_not_found(self):
        response = self.app.get('/jobs/1')
        expected_job = {
            'message': "Job 1 doesn't exist"
        }
        self.assert_response_not_found(response)
        job = self.deserialize(response.data)
        self.assertEquals(job, expected_job)
