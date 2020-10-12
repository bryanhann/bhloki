try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Also bump at eg.eg_util.VERSION
VERSION = '0.0.1'

LONG_DESCRIPTION = """ this is a long description"""

# The version here must match the version in the code itself. Currently they
# have to be updated in both places.
config = {
    'name': 'eg',
    'description': 'Examples at the command line',
    'long_description': 'a long description',
    'author': 'largo',
    'url': 'https://github.com/sbryanhann/pippy',
    'license': 'MIT',
    'author_email': 'largo@pobox.com',
    'version': VERSION,
    'install_requires': [],
    'test_requires': ['mock', 'pytest'],
    'packages': ['eg'],
    'scripts': ['bin/eg'],
    'package_data': {
        'eg': ['examples/*']
    },
    'zip_safe': False,
}

setup(**config)
