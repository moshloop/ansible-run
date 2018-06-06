from distutils.core import setup

setup(name='ansible-runner/', version='1.0', url='https://www/github.com/moshloop/ansible-runner',
    author='Moshe Immerman', author_email='firstname.surname@gmail.com',
  data_files=[('/usr/local/bin/ansible-runner', ['bin/ansible-runner'])])