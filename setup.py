#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages


setup(name='django-videothumbs',
    description='DjangoVideoThumbs',
    author='Chris McMichael',
    author_email='asermax@gmail.com',
    url="https://github.com/asermax/django-videothumbs",
    version='0.93',
    packages = find_packages(),
    long_description="DjangoVideoThumbs - Videos need thumbnails too",
    keywords="Django Video thumbnails",
    license="BSD"
)
