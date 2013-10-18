import json
import unittest

import get_a_job

class JobTestCase(unittest.TestCase):
    def setUp(self):
        self.app = get_a_job.app.test_client()

    def test_get_index(self):
        response = self.app.get('/')
        self.assertEquals(response.status_code, 200)
        empty_job = {
            "job": {
                "number_one": None,
                "number_two": None,
                "status": None,
                "links":[
                    {"href":"/jobs","rel":"index"}
                ]
            }
        }
        job = self.deserialize(response.data)
        self.assertEquals(job, empty_job)

    def deserialize(self, response):
        return json.loads(response)
