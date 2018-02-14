import unittest
from setuptools import setup, find_packages


def create_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite


setup_config = {
    'name': 'bitops',
    'version': '0.1',
    'packages': find_packages(exclude=[
        '*.tests',
        'test_*',
        'tests'
    ]),
    'author': 'Matthias Gilch',
    'author_email': 'matthias.gilch.mg@gmail.com',
    'keywords': 'bit bitwise operations ops operation',
    'test_suite': 'setup.create_test_suite'
}

if __name__ == '__main__':
    setup(**setup_config)
