# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import crakins
version = crakins.__version__

setup(
    name='crakins',
    version=version,
    author='',
    author_email='rakins@gmail.com',
    packages=[
        'crakins',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['crakins/manage.py'],
)