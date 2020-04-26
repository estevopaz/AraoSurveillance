#!/usr/bin/env python3
'''
AraoSL - Video Surveillance
'''

import os
from setuptools import setup


setup(
    name='AraoSL - Video Surveillance',
    version='1.0',
    author='Estevo Paz',
    author_email='estevo@araosl.com',
    description='Video Surveillance storage system',
    packages=[],
    scripts=['bin/' + script for script in os.listdir('bin')],
    keywords='python3',
    license='GPLv3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3',
        'Topic :: Python',
    ]
)
