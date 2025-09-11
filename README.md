# N&S python project/library cookiecutter template

Template for [cookiecutter](https://cookiecutter.readthedocs.io) so that
you can create a fresh plain python project or library.


## Using this cookiecutter template

Install/upgrade cookiecutter:

    $ pip install cookiecutter --upgrade

Run the following command and answer the questions:

    $ cookiecutter https://github.com/nens/cookiecutter-python-template


## Development of this template itself

Just do the regular:

    $ uv sync
    $ uv run pytest
    $ pre-commit run --all

The basic setup of [nens-meta](https://nens-meta.readthedocs.io/) should be used in this cookiecutter template, of course. You *can* run `uvx nens-meta` inside the `{{ cookiecutter.project_name }}/` directory, nens-meta is tweaked to work in such a directory.
