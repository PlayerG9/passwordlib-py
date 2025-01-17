# -*- coding=utf-8 -*-
r"""

"""
import sys; sys.path.append('src')  # noqa
from setuptools import setup
from passwordlib import __version__, __author__, __description__, __license__
import os.path as p

HERE = p.abspath(p.dirname(__file__))

install_requires = []

bcrypt_requires = ["bcrypt"]
all_requires = [bcrypt_requires]

extras_require = {
    'bcrypt': bcrypt_requires,
    'all': all_requires,
}

setup(
    name='password-library',
    version=__version__,
    description=__description__,
    long_description=open(p.join(HERE, 'README.md'), 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    author=__author__,
    license=__license__,
    url="https://github.com/PlayerG9/passwordlib-py/",
    project_urls={
        "Author Github": "https://github.com/PlayerG9",
        "Homepage": "https://github.com/PlayerG9/passwordlib-py/",
        "Bug Tracker": "https://github.com/PlayerG9/passwordlib-py/issues",
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Security",
        "Topic :: Utilities",
    ],
    package_data={
        # If any package contains *.txt files, include them:
        '': ['*.txt'],
    },
    python_requires=">=3.6",
    install_requires=install_requires,
    extras_require=extras_require,
    test_suite="tests",
)
