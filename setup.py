#!/usr/bin/env python
# coding: utf8


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybiopac",
    version="0.0.1",
    author="João Lamas",
    author_email="lamas.jp@gmail.com",
    description="pybiopac example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jplamas/pybiopac",
    packages=setuptools.find_packages(),
    classifiers=(
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Windows'
        'Topic :: Education',
        'Topic :: Research',
    ),
)
