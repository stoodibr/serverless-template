# coding: utf-8

# https://setuptools.readthedocs.io/en/latest/setuptools.html#basic-use

from setuptools import setup, find_packages
setup(
    name="serverless-template",
    version="0.1",
    packages=find_packages(),
    test_loader="unittest:TestLoader"
)
