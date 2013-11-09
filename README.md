Get A Job
=========

An Python implementation of "Get A Job" service from _Designing
Hypermedia APIs_ by Steve Klabnik.

Development
-----------

Install the package into a virtual environment:

    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements.txt

Running tests:

    $ python setup.py test

Create the database:

    $ python manage.py create_db

Start the server:

    $ python manage.py runserver
    * Running on http://127.0.0.1:5000/
    * Restarting with reloader

Start the background worker:

    $ python manager.py worker

Examples
--------

Introspect interface:

    $ curl --include http://127.0.0.1:5000/
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 111
    Server: Werkzeug/0.9.4 Python/2.7.5
    Date: Sat, 09 Nov 2013 22:43:48 GMT

    {
        "job": {
            "links": [
                {
                    "href": "/jobs",
                    "rel": "index"
                }
            ],
            "number_one": null,
            "number_two": null,
            "status": null
        }
    }

Create a job:

    $ curl --include \
           --data 'job[status]=in_progress' \
           --data 'job[number_one]=5' \
           --data 'job[number_two]=3' \
           http://127.0.0.1:5000/jobs
    HTTP/1.0 302 FOUND
    Content-Type: text/html; charset=utf-8
    Content-Length: 0
    Location: http://127.0.0.1:5000/jobs/1
    Server: Werkzeug/0.9.4 Python/2.7.5
    Date: Sat, 09 Nov 2013 22:37:27 GMT

Get the state of a job:

    $ curl --include http://127.0.0.1:5000/jobs/1
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 150
    Server: Werkzeug/0.9.4 Python/2.7.5
    Date: Sat, 09 Nov 2013 22:38:45 GMT

    {
        "job": {
            "links": [
                {
                    "href": "/jobs",
                    "rel": "index"
                },
                {
                    "href": "/jobs/1",
                    "rel": "self"
                }
            ],
            "number_one": 5,
            "number_two": 3,
            "status": "in_progress"
        }
    }

And once the background worker has processed the job:

    $ curl --include http://127.0.0.1:5000/jobs/1
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 160
    Server: Werkzeug/0.9.4 Python/2.7.5
    Date: Sat, 09 Nov 2013 22:42:01 GMT

    {
        "job": {
            "answer": 8,
            "links": [
                {
                    "href": "/jobs",
                    "rel": "index"
                },
                {
                    "href": "/jobs/1",
                    "rel": "self"
                }
            ],
            "number_one": 5,
            "number_two": 3,
            "status": "finished"
        }
    }
