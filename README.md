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
