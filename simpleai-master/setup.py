#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='simpleai',
    version='0.7.9',
    description=u'An implementation of AI algorithms based on aima-python',
    long_description=open('README.rst').read(),
    author = u'Juan Pedro Fisanotti',
    author_email = 'fisadev@gmail.com',
    url='http://github.com/simpleai-team/simpleai',
    packages=['simpleai', 'simpleai.search', 'simpleai.machine_learning'],
    package_data={'simpleai.search': ['web_viewer_resources/*.*']},
    license='LICENSE.txt',
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)
