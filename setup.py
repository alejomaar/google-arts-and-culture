from setuptools import find_packages, setup
#pipenv run pip install .
#pipenv run pip uninstall src -y
setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='Scraping',
    author='Alejandro Aponte',
    license='MIT',
)
