{{ cookiecutter.project_name }}
==========================================

Introduction

Usage, etc.


Installation
------------

We're installed with `pipenv <https://docs.pipenv.org/>`_, a handy wrapper
around pip and virtualenv. Install that first with ``pip install
pipenv``. Then run::

    $ PIPENV_VENV_IN_PROJECT=1 pipenv --three
    $ pipenv install

There will be a script you can run like this::

    $ pipenv run run-{{ cookiecutter.project_name }}

It runs the `main()` function in `{{ cookiecutter.project_name }}/scripts.py`,
adjust that if necessary. The script is configured in `setup.py` (see
`entry_points`).


Steps to do after generating with cookiecutter
----------------------------------------------

- Add a new project on https://github.com/nens/ with the same name. Set
  visibility to "public" and do not generate a license or readme.

  Note: "public" means "don't put customer data or sample data with real
  persons' addresses on github"!

- Follow the steps you then see (from "git init" to "git push origin master")
  and your code will be online.

- Go to
  https://github.com/nens/{{cookiecutter.project_name}}/settings/collaboration
  and add the teams with write access (you might have to ask someone with
  admin rights to do it).

- Update this readme. Use `.rst
  <http://www.sphinx-doc.org/en/stable/rest.html>`_ as the format.

- Remove this section as you've done it all :-)
