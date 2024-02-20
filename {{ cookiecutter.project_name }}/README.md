# {{ cookiecutter.project_name }}

Introduction

Usage, etc.

## Steps to do after generating with cookiecutter

- Add a new project on <https://github.com/nens/> with the same name.  Think
  about the visibility to ("public" / "private") and do not generate a
  license or readme.

  Note: "public" means "don't put customer data or sample data with real
  persons' addresses on github"!

- Follow the steps you then see (from "git init" to "git push origin main")
  and your code will be online.

- Go to
  https://github.com/nens/>{{ cookiecutter.project_name }}/settings/collaboration
  and add the teams with write access (you might have to ask someone with
  admin rights (like Reinout) to do it).

- Update this readme.

- Remove this section as you've done it all :-)


## Development installation of this project itself

We use python's build-in "virtualenv" to get a nice isolated
directory. You only need to run this once:

    $ python3 -m venv .venv

Activate the virtualenv and pip-install the requirements

    $ .venv/bin/activate   # Or "source .venv/bin/activate" on linux
    (.venv) $ pip install -r requirements.txt

Some commands:

    (.venv) $ tox -e lint  # Code format + checks
    (.venv) $ tox          # Checks, pytest, everything
    (.venv) $ pytest       # Just testing

If you need a new dependency (like `requests`), add it in
`pyproject.toml` in `dependencies`. And update your local install with:

    (.venv) $ pip install -r requirements.txt

For more instructions and vscode tips, see https://nens-meta.readthedocs.io/en/latest/usage.html .
