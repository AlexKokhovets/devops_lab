#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="snapshot",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'snapshot = snapshot.snapshot_script:start_monitoring', ],
    },
    version="0.1",
    author="Aliaksei Kakhavets",
    author_email="Aliaksei_Kakhavets@epam.com",
    description="App for monitoring the server",
    license="MIT"
)
