from __future__ import with_statement

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages


with open('README.rst') as readme:
    long_description = readme.read()


setup(
    name='Flask-Resource',
    version='0.0.1',
    author='Zachary Voase',
    author_email='z@zacharyvoase.com',
    url='https://github.com/zacharyvoase/flask-resource',
    description="Build resource-oriented Web apps with Flask.",
    long_description=long_description,
    packages=find_packages(exclude=('tests',)),
)
