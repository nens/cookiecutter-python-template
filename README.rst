N&S static site cookiecutter template
=====================================

Template for `cookiecutter <https://cookiecutter.readthedocs.io>`_ so that you
can create a fresh Django site project. It replaces the old "nensskel" tool.


Using this cookiecutter template
--------------------------------

Install/upgrade cookiecutter and pipenv::

  $ pip install cookiecutter --upgrade


Run the following command and answer the questions::

  $ cookiecutter https://github.com/nens/cookiecutter-staticsite-template


Development of this template itself
-----------------------------------

We don't need to run inside a vm/docker ourselves, so to set it up and test
it, just do the regular::

  $ PIPENV_VENV_IN_PROJECT=1 pipenv --three
  $ pipenv install --dev
  $ pipenv run pytest

The test, however, *does* use docker and docker-compose:

- There's a test that checks if the template itself generates OK without
  errors.

- There's a second test that uses the template-generated docker-compose setup
  to run the ``nosetests`` of the generated django.

We don't really need any python code ourselves, so our own ``setup.py``
doesn't actually point at any code. But it is set up so that ``nosetests``
finds and runs the tests inside ``./cookiecutter_tests/`` just fine.
