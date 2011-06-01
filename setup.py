#!/usr/bin/env python
try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

setup(
    name="sassypy",
    version="0.0",
    description="Featureful CSV handling",
    author="",
    author_email="",
    license="GPLv3",
    url="https://github.com/livingsocial/SassyPy",
    packages=["sassypy"],
    requires=[]
)
