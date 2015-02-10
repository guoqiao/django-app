import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-nzpower',
    version='0.1',
    packages=['nzpower'],
    license='MIT',
    description='A simple Django app.',
    long_description=README,
    url='https://github.com/guoqiao/django-nzpower',
    author='Guo Qiao',
    author_email='guoqiao@gmail.com',
    install_requires=[
        'path.py',
        'python-slugify',
        'django-annoying',
    ],
)
