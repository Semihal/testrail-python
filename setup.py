import sys
from setuptools import setup

install_requires=[
    'requests>=2.6.0',
    'singledispatch>=3.4.0',
    'pyyaml>=3.1.1',
]

if sys.version_info[:3] < (2, 7, 0):
    install_requires.append('ordereddict')

setup(
    name='testrail',
    packages=['testrail'],
    version='0.2.2',
    description='Python library for interacting with TestRail via REST APIs.',
    author='Travis Pavek',
    author_email='travis.pavek@gmail.com',
    url='https://github.com/travispavek/testrail-python',
    download_url='https://github.com/travispavek/testrail-python/tarball/0.2.2',
    keywords=['testrail', 'api', 'client', 'library', 'rest'],
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
