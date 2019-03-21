#!/usr/bin/env python
import os
from setuptools import setup

from beanstalkc import __version__ as src_version

PKG_VERSION = os.environ.get('BEANSTALKC_PKG_VERSION', src_version)

setup(
    name='beanstalkc3-ot',
    version=PKG_VERSION,
    py_modules=['beanstalkc'],

    author='Andreas Bolka',
    author_email='a@bolka.at',
    description='A simple beanstalkd client library',
    long_description='''
beanstalkc3-ot is a simple beanstalkd client library for Python3. `beanstalkd
<https://beanstalkd.github.io>`_ is a fast, distributed, in-memory
workqueue service.
''',
    url='https://github.com/jpmens/beanstalkc3-ot',
    license='Apache License, Version 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
