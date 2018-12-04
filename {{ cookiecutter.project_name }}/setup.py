from setuptools import setup

version = "0.1.dev0"

long_description = "\n\n".join([open("README.rst").read(), open("CHANGES.rst").read()])

install_requires = []

tests_require = ["pytest", "coverage", "mock"]

setup(
    name="{{ cookiecutter.project_name }}",
    version=version,
    description="{{ cookiecutter.project_short_description }}",
    long_description=long_description,
    # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=["Programming Language :: Python", "Framework :: Django"],
    keywords=[],
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    url="",
    license="MIT",
    packages=["{{ cookiecutter.package_name }}"],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={"test": tests_require},
    entry_points={"console_scripts": []},
)
