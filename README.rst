N&S python project/library cookiecutter template
================================================

Template for `cookiecutter <https://cookiecutter.readthedocs.io>`_ so that you
can create a fresh plain python project or library.


Using this cookiecutter template
--------------------------------

Install/upgrade cookiecutter::

  $ pip install cookiecutter --upgrade


Run the following command and answer the questions::

  $ cookiecutter https://github.com/nens/cookiecutter-python-template


Development of this template itself
-----------------------------------

Just do the regular::

  $ python3 -m venv .
  $ bin/pip install -r requirements.txt
  $ pre-commit install
  $ bin/pytest
