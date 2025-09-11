import os
import shutil
import subprocess
import sys
import tempfile
import unittest

from cookiecutter.main import cookiecutter


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.mkdtemp(prefix="python-template")
        self.cookiecutter_dir = os.getcwd()
        os.chdir(self.tempdir)
        cookiecutter(
            self.cookiecutter_dir,
            no_input=True,
            extra_context={"project_name": "my-project"},
        )

    def tearDown(self):
        os.chdir(self.cookiecutter_dir)
        shutil.rmtree(self.tempdir)

    def test_smoke(self):
        assert "my-project" in os.listdir()

    def test_generated_project(self):
        os.chdir("my-project")
        # We have to pass a full string instead of clean splitted ([...])
        # arguments as otherwise calling python from within our own python
        # interferes too much.
        subprocess.run(f"{sys.executable} -m venv .", shell=True, check=True)
        subprocess.run("bin/pip install -e .[test]", shell=True, check=True)
        subprocess.run("bin/pytest", shell=True, check=True)

    def test_lint_generated_project(self):
        os.chdir("my-project")
        subprocess.run("git init", shell=True, check=True)
        subprocess.run("git add -A", shell=True, check=True)
        # "sys.executable -m pre_commit" is the same as calling "pre-commit",
        # but in a way that's handier for testing as we can add pre-commit as
        # a test dependency that way.
        subprocess.run(
            f"{sys.executable} -m pre_commit install", shell=True, check=True
        )
        subprocess.run(
            f"{sys.executable} -m pre_commit run -av", shell=True, check=True
        )

    def test_pyupgrade_generated_project(self):
        os.chdir("my-project")
        subprocess.run("git init", shell=True, check=True)
        subprocess.run("git add -A", shell=True, check=True)
        try:
            subprocess.run(
                f"{sys.executable} -m pyupgrade --py38-plus my_project/*py",
                shell=True,
                check=True,
            )
        except subprocess.CalledProcessError:
            subprocess.run("git diff", shell=True, check=True)
            raise
