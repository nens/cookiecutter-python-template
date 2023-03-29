from cookiecutter.main import cookiecutter

import os
import shutil
import subprocess
import sys
import tempfile
import unittest


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.mkdtemp(prefix="python-template")
        self.cookiecutter_dir = os.getcwd()
        os.chdir(self.tempdir)
        cookiecutter(
            self.cookiecutter_dir,
            no_input=True,
            extra_context={
                "project_name": "my-project"
            },
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
        subprocess.run("%s -m venv ." % sys.executable, shell=True, check=True)
        subprocess.run("bin/pip install -e .[test]", shell=True, check=True)
        subprocess.run("bin/pytest", shell=True, check=True)

    def test_lint_generated_project(self):
        os.chdir("my-project")
        subprocess.run("git init", shell=True, check=True)
        subprocess.run("git add -A", shell=True, check=True)
        subprocess.run("pre-commit install", shell=True, check=True)
        subprocess.run("pre-commit run -av", shell=True, check=True)
