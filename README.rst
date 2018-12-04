N&S python project/library cookiecutter template
================================================

Template for `cookiecutter <https://cookiecutter.readthedocs.io>`_ so that you
can create a fresh plain python project or library.


Using this cookiecutter template
--------------------------------

Install/upgrade cookiecutter and pipenv::

  $ pip install cookiecutter --upgrade


Run the following command and answer the questions::

  $ cookiecutter https://github.com/nens/cookiecutter-python-template


Development of this template itself
-----------------------------------

Just do the regular::

  $ PIPENV_VENV_IN_PROJECT=1 pipenv --three
  $ pipenv install --dev
  $ pipenv run pytest
