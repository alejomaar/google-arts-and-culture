from setuptools import find_packages, setup
#pipenv install -e .
#pipenv run pip uninstall src -y
setup(
    name='src',
    packages=find_packages(where='src'),
    version='0.1.0',
    description='Scraping',
    author='Alejandro Aponte',
    license='MIT',
)
