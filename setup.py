from setuptools import find_packages
from setuptools import setup
from setuptools.command.install import install

setup(
    name="eagle-test-graphs",
    version="0.0.1",
    packages=find_packages(where="graphs"),
    package_dir={"": "graphs"},
    package_data={"eagle-test-graphs" :["*.graph", "*.pkl", "*.json"]}
)
