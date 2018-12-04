from cookiecutter.main import cookiecutter

import os
import shutil
import tempfile
import unittest


class BasicTest(unittest.TestCase):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp(prefix='staticsite')
        self.cookiecutter_dir = os.getcwd()
        os.chdir(self.tempdir)

    def tearDown(self):
        os.chdir(self.cookiecutter_dir)
        shutil.rmtree(self.tempdir)

    def test_smoke(self):
        cookiecutter(
            self.cookiecutter_dir,
            no_input=True,
            extra_context={'email': 'your.name@nelen-schuurmans.nl'})
