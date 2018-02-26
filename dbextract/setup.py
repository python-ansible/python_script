# _*_ coding: utf-8 _*_
import os

from setuptools import find_packages
from setuptools import setup

base_dir = os.path.dirname(__file__)
setup(
    name='dbextract',
    version='0.0.1',
    description='use for cs,portal,nsp db extract.',
    author='wangzelin',
    author_email='wangzelin007@pingan.com.cn',
    setup_requires='setuptools',
    license='Copyright 2017 PACloud',
    entry_points={
	'console_scripts':['dbextract=dbextract.all:main']},
    data_files=[('/etc/dbextract',['etc/config.json'])],
    packages=find_packages(),
    classifiers=[
	'Development Status :: 5 - Production/Stable',
	'Programming Language :: Python :: 2.6',
	'Programming Language :: Python :: 2.7',
        'Topic ::System :: Networking',
	'Intended Audience :: Developers',
	'Operating System :: OS Independent',
	'Topic :: Software Development :: Libraries :: Python Modules',
        ]
)
