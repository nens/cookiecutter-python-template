from setuptools import setup

version = '0.1.dev0'

install_requires = [
    'cookiecutter',
    'pytest',  # pipenv doesn't install test_requires.
    ]

tests_require = [
    ]

setup(
    name='cookiecutter-staticsite-template',
    packages=[],
    version=version,
    description='Cookiecutter template for a static site',
    author='Reinout van Rees',
    license='MIT',
    author_email='reinout@vanrees.org',
    url='https://github.com/nens/cookiecutter-staticsite-template',
    keywords=['cookiecutter', 'template', 'package', ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
    ],
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'test': tests_require},
)
