"""A setuptools based setup module for dummy_app.
Setup configuration is read from setup.cfg.

For a detailed explanation of setup options see:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
setuptools.readthedocs.io
"""
import os
from setuptools import setup
from setuptools.config import read_configuration

def set_version():
    here = os.path.abspath(os.path.dirname(__file__))
    config = read_configuration(os.path.join(here,'setup.cfg'))
    version = config['metadata']['version']
    try:
        branch_name = os.environ['BRANCH_NAME']
        if branch_name != "dev":
            version = version.replace("dev", "dev-"+branch_name)
    except KeyError:
        pass
    return version

# Run build.
setup(version=set_version())
