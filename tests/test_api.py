import json
import unittest

from get_a_job import create_app
from get_a_job.models import db, Job

SQLALCHEMY_DATABASE_URI = 'sqlite://'


class TestCase(unittest.TestCase):

    def setUp(self):
        app = create_app(__name__)
        self.app = app.test_client()
        db.app = app
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def deserialize(self, response):
        return json.loads(response)

    def assert_redirected(self, response, location):
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.headers.get('Location'), location)

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
        self.assert_redirected(response, 'http://localhost/jobs/1')
        self.assert_persisted(id=1, job=Job(1, 2, 'in_progress'))

    def assert_persisted(self, id, job):
        jobs = Job.query.filter_by(id=id)
        self.assertEqual(jobs.count(), 1)
        self.assertEquals(jobs[0], job)
