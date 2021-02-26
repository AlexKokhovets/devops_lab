from setuptools import setup, find_packages

setup(
    name="snapshot",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'snapshot = sc.task1:start_monitoring',
	],	
    }, 
    version="0.1",
    author="Aliaksei Kakhavets",
    author_email="Aliaksei_Kakhavets@epam.com",
    description="App for monitoring the server",
    license="MIT"
)
