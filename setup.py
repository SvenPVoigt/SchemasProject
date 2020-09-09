from distutils.core import setup
from setuptools import find_packages

setup(
    name='SchemasProject',
    version='0.1.0',
    packages=find_packages(),
    license='The MIT License (MIT)',
    long_description=open('README.md').read(),
    author='Sven Voigt',
    author_email='svenpvoigt@gmail.com',
    url='http://pypi.python.org/pypi/SchemasProject/',
    description='Standardized Schemas for Python Classes from Open-Source Projects.',
    scripts=['bin/imagemks', 'bin/cellanalysis'],
    python_requires=">=3.6",
    install_requires=[
        'pydantic'
    ],
)
