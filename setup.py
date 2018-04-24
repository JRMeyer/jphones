from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

    # Arguments marked as "Required" below must be included for upload to PyPI.
    # Fields marked as "Optional" may be commented out.
    
setup(
    name='jphones',
    version='1.0.0',
    description='A Japanese phonetizer',
    packages=find_packages('.'),
)

    

