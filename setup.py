#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

from setuptools import find_packages, setup

try:
    import pypandoc
    readme = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    readme = ''

# package variables
package = 'tapioca_discourse'
requirements = [
    'tapioca-wrapper<2',
]
test_requirements = [
]

# dynamic package info
init_py = open(os.path.join(package, '__init__.py')).read()
version = re.search(
    "^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)
author = re.search(
    "^__author__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)
email = re.search(
    "^__email__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)

setup(
    name='tapioca-discourse',
    version=version,
    description='discourse API wrapper using tapioca',
    long_description=readme,
    author=author,
    author_email=email,
    url='https://github.com/humrochagf/tapioca-discourse',
    packages=find_packages(),
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords=['api', 'discourse', 'web'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
