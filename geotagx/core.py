# The GeoTag-X command line toolkit.
# This module contains the toolkit's entry point.
#
# Copyright (c) 2016 UNITAR/UNOSAT
#
# The MIT License (MIT)
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.
def init_argument_parser():
	"""Initializes the toolkit's command line argument parser."""
	from __init__ import __version__
	import argparse
	parser = argparse.ArgumentParser(
		prog="geotagx",
		description="A set of tools that help manage a GeoTag-X server.",
		add_help=False
	)
	parser.set_defaults(handler=None)
	options = parser.add_argument_group("OPTIONS")
	options.add_argument("-h", "--help", action="help", help="Display this help and exit.")
	options.add_argument("--version", action="version", help="Display version information and exit.", version="""
		GeoTag-X Command Line Toolkit v%s, Copyright (C) UNITAR/UNOSAT.
	""" % __version__)

	return parser


def main(argv=None):
	import sys
	# import geotagx.build.core
	import geotagx.sanitize.core

	parser = init_argument_parser()

	# Initialize each tool's argument parser.
	subparsers = parser.add_subparsers(
		title="COMMANDS",
		metavar="",
		description="The following is a set of commands you can use to select a specific tool.",
		prog="geotagx"
	)
	parents = [parser]
	initializers = [
		# geotagx.build.core.init_argument_parser,
		geotagx.sanitize.core.init_argument_parser
	]
	for initializer in initializers:
		initializer(subparsers, parents)

	arguments = parser.parse_args(sys.argv[1:] if argv is None else argv)

	# Make sure the 'handler' argument is callable (a function or method).
	run = arguments.handler
	if not hasattr(run, "__call__"):
		parser.error("The 'handler' argument is not callable.")

	run(arguments)
	return 0
