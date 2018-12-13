from cookiecutter.main import cookiecutter

import os
import shutil
import subprocess
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
                "project_name": "my-project",
                "email": "your.name@nelen-schuurmans.nl",
            },
        )

    def tearDown(self):
        os.chdir(self.cookiecutter_dir)
        shutil.rmtree(self.tempdir)

    def test_smoke(self):
        assert "my-project" in os.listdir()

    def test_generated_project(self):
        os.chdir("my-project")
        subprocess.run(["pipenv", "--three"], shell=True, check=True)
        subprocess.run(["pipenv", "install"], shell=True, check=True)
        subprocess.run(["pipenv", "run", "pytest"], shell=True, check=True)
