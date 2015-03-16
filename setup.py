#!/usr/bin/env python

from os.path import exists
from setuptools import setup
import re

version_raw    = open('glopen/_version.py').read()
version_regex  = r"^__version__ = ['\"]([^'\"]*)['\"]"
version_result = re.search(version_regex, version_raw, re.M)
if version_result:
    version_string = version_result.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))


setup(name='glopen',
      version=version_string,
      description='Open-like interface to globus remotes',
      url='http://github.com/maxhutch/glopen/',
      author='https://raw.github.com/maxhutch/glopen/master/AUTHORS.md',
      author_email='maxhutch@gmail.com',
      maintainer='Max Hutchinson',
      maintainer_email='maxhutch@gmail.com',
      license='MIT',
      keywords='globus ssh open',
      install_requires=list(open('requirements.txt').read().strip()
                            .split('\n')),
      long_description=(open('README.rst').read() if exists('README.rst')
                              else ''),
      packages=['glopen'],
      zip_safe=True)
