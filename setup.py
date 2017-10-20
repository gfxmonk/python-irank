#!/usr/bin/env python

import os
from setuptools import *
here = os.path.dirname(__file__)
setup(
	name='irank',
	version='0.3.2',
	author='Tim Cuthbertson',
	description="music ranking metadata manager",
	packages = find_packages(exclude=['test', 'test.*']),
	scripts = ['bin/irank'] + [os.path.join('bin', f) for f in os.listdir(os.path.join(here, 'bin'))],
	package_data = {
		'irank': ['../VERSION'],
	},
	data_files = [
		('libexec/irank', ['libexec/irank/mpris-display']),
	],
	install_requires=[
		'setuptools',
		'mutagen',
		'pyyaml',
	],
)
