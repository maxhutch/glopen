#!/usr/bin/env python

from os.path import exists
from setuptools import setup
import glopen

setup(name='glopen',
      version=glopen.__version__,
      description='Pickle-like interface to globus remotes',
      url='http://github.com/maxhutch/glopen/',
      author='https://raw.github.com/maxhutch/glopen/master/AUTHORS.md',
      author_email='maxhutch@gmail.com',
      maintainer='Max Hutchinson',
      maintainer_email='maxhutch@gmail.com',
      license='MIT',
      keywords='globus pickle ssh',
      packages=['glopen'],
      zip_safe=True)
