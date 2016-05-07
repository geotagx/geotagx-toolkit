#!/usr/bin/env python
#
# This setup script is inspired by code from the Pip setup.py found
# here: https://github.com/pypa/pip/blob/develop/setup.py
import os, re, codecs
from setuptools import setup, find_packages

cwd = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
	# intentionally *not* adding an encoding option to open, See:
	# https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
	return codecs.open(os.path.join(cwd, *parts), 'r').read()


def find_version(*file_paths):
	version_file = read(*file_paths)
	version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
	if version_match:
		return version_match.group(1)
	raise RuntimeError("Unable to find version string.")


setup(
	name="geotagx-toolkit",
	version=find_version("geotagx", "__init__.py"),
	description="The GeoTag-X command line toolkit.",
	long_description=read("README.md"),
	zip_safe=True,
	install_requires=[
		"geotagx_builder",
		"geotagx_sanitizer>=0.0.5",
	],
	dependency_links=[
		"https://github.com/othieno/geotagx-tool-sanitizer/archive/v0.0.5.tar.gz#egg=geotagx_sanitizer-0.0.5",
	],
	# keywords="",
	# author="",
	# author_email="",
	# maintainer="",
	# maintainer_email="",
	url="https://github.com/geotagx/geotagx-toolkit",
	download_url="https://github.com/geotagx/geotagx-toolkit",
	# classifiers=[],
	# platforms=[],
	license="MIT",
	packages=find_packages(),
	entry_points={
		"console_scripts":[
			"geotagx=geotagx.core:main",
		],
	}
)
