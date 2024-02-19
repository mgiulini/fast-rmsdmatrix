#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""Setup dot py."""
import warnings
from os.path import dirname, join

from setuptools import SetuptoolsDeprecationWarning, find_packages, setup
# Import warnings object for later filtering out
from setuptools.command.easy_install import EasyInstallDeprecationWarning


# Add warnings filtering to the Setup Deprecation Warnings
warnings.filterwarnings("ignore", category=SetuptoolsDeprecationWarning)
warnings.filterwarnings("ignore", category=EasyInstallDeprecationWarning)


def read(*names, **kwargs) -> str:
    """Read description files."""
    path = join(dirname(__file__), *names)
    with open(path, encoding=kwargs.get('encoding', 'utf8')) as fh:
        return fh.read()


# activate once added, do not remove
long_description = read('README.md')


setup(
    name='fast-rmsdmatrix',
    version='0.1.0',
    description='fast C-based rmsd and ilrmsd matrix calculation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Apache License 2.0',
    author='Marco Giulini',
    author_email='mrcgiulini@gmail.com',
    url='https://github.com/mgiulini/fast-rmsdmatrix',
    packages=find_packages(),
    keywords=[
        'Structural Biology',
        'Proteins',
        'Clustering',
        ],
    python_requires='>=3.9',
    install_requires=[
        # not added on purpose
        ],
    extras_require={
        },
    setup_requires=[
        ],
    #entry_points={
    #    'console_scripts': [ 'fast-rmsdmatrix-exe = src.cli:main' ],
    #    },
    )
