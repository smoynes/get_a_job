# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

requirements = [
    'Flask==0.10.1',
    'Flask-RESTful==0.2.5',
    # Undeclared dependency from Flask-RESTful
    'six == 1.2.0',
    'Flask-SQLAlchemy==0.8.2',
]

test_requirements = [
    'nose==1.3.0',
]

setup(
    name='get_a_job',
    version='0.0.1',
    description='Hypermedia Job Service',
    long_description=readme,
    author='Scott Moynes',
    author_email='scott.moynes@gmail.com',
    url='https://github.com/smoynes/get_a_job',
    license=license,
    packages=find_packages(exclude=['tests']),
    test_suite='nose.collector',
    install_requires=requirements,
    setup_requires=test_requirements,
)
