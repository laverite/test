# -*- coding: utf-8 -*-
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, '.')
from test import __version__


setup(
    name="test",
    version=__version__,
    description="Flask based microservice.",
    maintainer="",
    packages=["test", "test.testAPp"],
    platforms=["any"]
)
