from __future__ import absolute_import

from celery.signals import task_postrun
from .config import celery, db
from .models import Job

@celery.task(name='get_a_job.add_number')
def add_number(job):
    db.session.add(job)
    job.answer = job.number_one + job.number_two
    job.status = 'finished'
    db.session.commit()

@task_postrun.connect
def remove_session(*args, **kwargs):
    db.session.remove()
