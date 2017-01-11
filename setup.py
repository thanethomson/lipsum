#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Setup script for lipsum - a Python-based Lorem Ipsum text generator.
"""

from setuptools import setup
from lipsum import __version__

setup(
    name="lipsum",
    version=__version__,
    description="A randomised Lorem Ipsum generator library for Python",
    author="Thane Thomson",
    author_email="connect@thanethomson.com",
    url="https://github.com/thanethomson/lipsum",
    packages=["lipsum"],
    package_data={
        "lipsum": [
            "data/*.txt"
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Utilities"
    ]
)
