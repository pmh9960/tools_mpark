## setup.py
from glob import glob
from os.path import basename, splitext
from setuptools import find_packages, setup

setup(
    name='tools_mpark',
    version='0.1',
    packages=find_packages(where='tools_mpark'),
    package_dir={'': 'tools_mpark'},
    py_modules=[splitext(basename(path))[0] for path in glob('tools_mpark/*.py')],
)