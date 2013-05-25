#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.5',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

REQUIREMENTS = [
    'Django >= 1.3',
    'pillow >= 1.7.8',
]

setup(name='django-tits',
      author='Jesús Espino',
      author_email='jespinog@gmail.com',
      description='Transparent image transformation system',
      license='BSD',
      version=':versiontools:django_tits:',
      setup_requires = [
          'versiontools >= 1.8',
      ],
      packages=find_packages(),
      include_package_data=True,
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      platforms=['any'])
