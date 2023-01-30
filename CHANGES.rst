Changelog for cookiecutter-python-template
==========================================


0.5 (unreleased)
----------------

- Added pre-commit and 'lint' github action. Updated flake8 and isort settings.

- Upgraded the 'test' github action.

- Added a {{ package_name }}.__version__.

- Hard code 'full_name' and 'email' to "Nelen & Schuurmans" and "info@nelen-schuurmans.nl".


0.4 (2020-03-23)
----------------

- Removed ``.travis.yml`` file from generated project.

- Fixed github actions dirname.

- Added proper secret-based coveralls.io setup.


0.3 (2020-03-23)
----------------

- Moved from travis-ci to github actions.


0.2 (2020-03-03)
----------------

- Switched from pipenv to plain virtualenv+pip.

- Fixed the test setup so that running the tests for the generated project
  would really actually run the tests :-)


0.1 (2019-01-16)
----------------

- Started the project.

- Updated the generated project structure after experience with the first
  project that used it.
