
from subprocess import *
from setuptools import setup, find_packages
import os

setup(
    name = 'ansible-run', version = '3.3',
    url = 'https://www/github.com/moshloop/ansible-run',
    author = 'Moshe Immerman', author_email = 'firstname.surname@gmail.com',
    scripts = ['ansible-run', 'ansible-test', 'ansible-role', 'ansible-vault-run']
    )