from setuptools import setup

def readme():
  with open("README.md") as f:
    return f.read()

setup(
  name = "isbit_client",
  version = "1.0.0",
  description = "Python client for ISBIT Exchange",
  url = 'https://github.com/ISBITX/isbit-client-python',
  long_description = readme(),
  author = "ISBITX",
  license = "GPL",
  keywords = "isbit mexico fintech bigdata ai blockchain",
  test_suite = "tests",
  packages = [
    "isbit_client"],
  install_requires = [
    "requests"],
  zip_safe = False)
