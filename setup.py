""" """
from setuptools import find_packages
from setuptools import setup


setup(
    name="hello_microservice",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'aiohttp',
        'gunicorn'
    ]
)
