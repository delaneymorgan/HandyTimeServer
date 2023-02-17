from setuptools import setup, find_packages
import src


with open("DESCRIPTION.txt") as file:
    long_description = file.read()

REQUIREMENTS = []

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Utility',
    'License :: Freeware',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
],

setup(
    name=src.__name__,
    version=src.__version__,
    description='A simple python local time server',
    packages=find_packages(),
    zip_safe=True,
    url='https://github.com/delaneymorgan/LocalTimeServer',
    author='Craig McFarlane',
    author_email='support@delaneymorgan.com.au',
    license='Freeware',
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS
)
