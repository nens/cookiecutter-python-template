# N&S python project/library cookiecutter template

Template for [cookiecutter](https://cookiecutter.readthedocs.io) so that
you can create a fresh plain python project or library.


## Using this cookiecutter template

Install/upgrade cookiecutter:

    $ uv tool install cookiecutter --upgrade

Run the following command and answer the questions:

    $ cookiecutter https://github.com/nens/cookiecutter-python-template

This cookiecutter can also generate a django project for you:

    $ cookiecutter --directory django https://github.com/nens/cookiecutter-python-template


## Development of this template itself

Just do the regular:

    $ uv sync
    $ uv run pytest
    $ pre-commit run --all

The basic setup of [nens-meta](https://nens-meta.readthedocs.io/) should be used in this cookiecutter template, of course. You *can* run `uvx nens-meta` inside the `{{ cookiecutter.project_name }}/` directory, nens-meta is tweaked to work in such a directory.

The `django/` directory contains customisations to work with django projects. I wanted to keep most of the files the same, of course. This is done with symlinks. From time to time, run the script that syncs django to the regular template:

    $ uv run symlink_into_django_template.py

It will create missing symlinks, show which files are existing symlinks and which files are custom. The custom files are printed with `diff -u` instructions so that you can easily spot the differences.
