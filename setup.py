from setuptools import find_packages
from setuptools import setup
from setuptools.command.install import install

setup(
    name="eagle-test-graphs",
    version="0.0.1",
    packages=["graphs"],
    package_data={
        "graphs.daliuge_tests": ["*.pkl"],
    }
)
