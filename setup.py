from setuptools import setup, find_packages

setup(
    name='pre-commit-hooks',
    version='0.1.0',
    description='custom pre commit hooks',
    author='Gai Radzi',
    author_email='gairazdi@kennethreitz.com',
    url='https://github.com/gairadzi/pre-commit-hooks',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'validate-webservers-schema = pre_commit_hooks.validate_webservers_schema:main'
        ]
    }
)
