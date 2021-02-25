from setuptools import setup, find_packages

setup(
    name="devops_lab",
    packages=find_packages(),
    scripts=["task2.1.py"],
    version="0.1",
    author="Aliaksei Kakhavets",
    author_email="Aliaksei_Kakhavets@epam.com",
    description="App for monitoring the server",
    license="MIT"
)