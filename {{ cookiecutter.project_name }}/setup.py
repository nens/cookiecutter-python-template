from setuptools import setup, find_packages
import pathlib

long_description = "\n\n".join([open("README.rst").read(), open("CHANGES.rst").read()])

def get_version():
    # Edited from https://packaging.python.org/guides/single-sourcing-package-version/
    init_path = pathlib.Path(__file__).parent / "{{ cookiecutter.package_name }}/__init__.py"
    for line in init_path.open("r").readlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


install_requires = []

tests_require = ["pytest", "pytest-cov"]

setup(
    name="{{ cookiecutter.project_name }}",
    version=get_version(),
    description="{{ cookiecutter.project_short_description }}",
    long_description=long_description,
    # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=["Programming Language :: Python", "Framework :: Django"],
    keywords=[],
    author="Nelen & Schuurmans",
    author_email="info@nelen-schuurmans.nl",
    url="https://github.com/nens/{{ cookiecutter.project_name }}",
    license="MIT",
    packages=[find_packages("{{ cookiecutter.package_name }}*")],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    python_requires=">=3.7",
    tests_require=tests_require,
    extras_require={"test": tests_require},
    entry_points={
        "console_scripts": [
            "run-{{ cookiecutter.project_name }} = {{ cookiecutter.package_name }}.scripts:main"
        ]
    },
)
