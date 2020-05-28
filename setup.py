# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in mawaq/__init__.py
from mawaq import __version__ as version

setup(
	name='mawaq',
	version=version,
	description='This application help to Mawaq organization',
	author='Aadhil',
	author_email='aadhilpm@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
