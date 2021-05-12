import sys
from setuptools import setup, find_packages

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    raise RuntimeError('Python 3.6 at least required')

install_requires = [
    'Flask==2.0.0',
]

setup(name='sonarcloud-flask-demo',
      version='1.0',
      install_requires=install_requires,
      packages=find_packages())