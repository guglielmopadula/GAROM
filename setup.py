"""
setup.py
"""
from setuptools import setup, find_packages

# Package meta-data.
NAME = 'garom'
DESCRIPTION = 'GAROM (fork)'
URL = 'https://github.com/gpadula/GAROM'
MAIL = 'gpadula@sissa.it'
AUTHOR = 'Guglielmo Padula'
VERSION = '0'
KEYWORDS = 'dimension_reduction mathematics generative_adversarial_networks'

REQUIRED = [
    'future', 'numpy',
]


LDESCRIPTION = (
"")


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LDESCRIPTION,
    author=AUTHOR,
    author_email=MAIL,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Mathematics'
    ],
    keywords=KEYWORDS,
    url=URL,
    license='MIT',
    packages=find_packages(),
    install_requires=REQUIRED,
    include_package_data=True,
    zip_safe=False,
)
