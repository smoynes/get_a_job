import json
import unittest

from get_a_job import create_app
from get_a_job.models import db

SQLALCHEMY_DATABASE_URI = 'sqlite://'


class TestCase(unittest.TestCase):

    def setUp(self):
        app = create_app(__name__)
        self.app = app.test_client()
        db.app = app
        db.create_all()

    def deserialize(self, response):
        return json.loads(response)


class JobListTestCase(TestCase):

    def test_get_index(self):
        response = self.app.get('/')
        self.assertEquals(response.status_code, 200)
        empty_job = {
            "job": {
                "number_one": None,
                "number_two": None,
                "status": None,
                "links":[
                    {"href":"/jobs", "rel":"index"}
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
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.headers.get('Location'), 'http://localhost/jobs/1')
