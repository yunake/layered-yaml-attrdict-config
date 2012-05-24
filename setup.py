#!/usr/bin/env python

from setuptools import setup, find_packages
import os

pkg_root = os.path.dirname(__file__)

setup(

	name = 'layered-yaml-attrdict-config',
	version = '12.05.1',
	author = 'Mike Kazantsev',
	author_email = 'mk.fraggod@gmail.com',
	license = 'WTFPL',
	keywords = 'yaml configuration conf serialization inheritance merge update',
	url = 'https://github.com/mk-fg/layered-yaml-attrdict-config',

	description = 'YAML-based configuration module',
	long_description = open(os.path.join(pkg_root, 'README.md')).read(),

	classifiers = [
		'Development Status :: 4 - Beta',
		'Framework :: Twisted',
		'Intended Audience :: Developers',
		'Intended Audience :: Information Technology',
		'Intended Audience :: System Administrators',
		'License :: OSI Approved',
		'Operating System :: POSIX',
		'Operating System :: Unix',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 2 :: Only',
		'Topic :: Software Development',
		'Topic :: Software Development :: Libraries :: Python Modules' ],

	install_requires = ['PyYAML'],
	packages = find_packages() )