# Dockerfile for running tests on jenkins.
FROM python:3.6
WORKDIR /code
RUN pip install --upgrade setuptools pip
RUN pip install pipenv
ADD . /code
RUN rm -rf .venv
RUN pipenv lock
RUN PIPENV_VENV_IN_PROJECT=1 pipenv sync --dev
