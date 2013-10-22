Get A Job
=========

An Python implementation of "Get A Job" service from _Designing
Hypermedia APIs_ by Steve Klabnik.

Installation
------------

From source:

    $ python setup.py install

Development
-----------

    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    $ python setup.py develop

Running tests:

    $ python setup.py test

Start the server:

    $ python manage.py create_db
    $ python manage.py runserver
    * Running on http://127.0.0.1:5000/
    * Restarting with reloader
