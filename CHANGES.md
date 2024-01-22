# Changelog for cookiecutter-python-template


## 0.6 (unreleased)


- Requiring python 3.10 in the generated project.

- Moved to ruff: this includes black, isort, pyflakes and
  pyupgrade. Including configuration that enables it.

- Setup.cfg is gone now, everything is in pyproject.toml.

- Documenting that you should generate the virtualenv in the `./venv`
  dir instead of directly in `.`, this matches the python.org docs.

- Added initial configuration for pyright/pylance, this helps vscode
  and other LSP-using editors. (partially helped by the abovementioned
  `./venv` change).

- Updated github actions and added the dependabot "github action
  autoupdater".


## 0.5 (2023-03-29)

- Added pre-commit and 'lint' github action. Updated flake8 and isort settings.

- Upgraded the 'test' github action.

- Added a `{{ package_name }}.__version__`.

- Hard code 'full_name' and 'email' to "Nelen & Schuurmans" and
  "info@nelen-schuurmans.nl".

- Changed the template itself and the package it generates to use pyproject.toml
  instead of setup.py as per PEP 621. Setup.cfg is retained for a few settings.

- Added "Nelen & Schuurmans" and "info@nelen-schuurmans.nl" as author and email
  for the template itself.

- Added pre-commit to ourselves for basic checks.

- Added basic end-of-file and trailing-whitespace checks and so to the
  generated project's pre-commit hooks.

- Fixed master/main branch naming.

- Testing the generated project with its generated pre-commit hooks to make
  sure it is in tip-top shape right from the start.

- Swiched from `.rst` to markdown.


## 0.4 (2020-03-23)

- Removed `.travis.yml` file from generated project.

- Fixed github actions dirname.

- Added proper secret-based coveralls.io setup.


## 0.3 (2020-03-23)

- Moved from travis-ci to github actions.


## 0.2 (2020-03-03)

- Switched from pipenv to plain virtualenv+pip.

- Fixed the test setup so that running the tests for the generated project
  would really actually run the tests :-)


## 0.1 (2019-01-16)

- Started the project.

- Updated the generated project structure after experience with the first
  project that used it.
