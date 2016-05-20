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
def _init_argparser():
    """Initializes the toolkit's command line argument parser."""
    from __init__ import __version__
    import argparse

    parser = argparse.ArgumentParser(
        prog="geotagx",
        description="A set of tools that help manage a GeoTag-X server.",
        add_help=False
    )
    options = parser.add_argument_group("OPTIONS")
    options.add_argument("-h", "--help", action="help", help="Display this help and exit.")
    options.add_argument("-v", "--version", action="version", help="Display version information and exit.", version=_version())

    return parser


def _version():
    """Returns the project's version string."""
    from __init__ import __version__
    return "GeoTag-X Command Line Toolkit v%s, Copyright (C) 2016 UNITAR/UNOSAT." % __version__


def main(argv=None):
    import sys
    import geotagx_builder.builder as builder
    import geotagx_sanitizer.sanitizer as sanitizer

    parser = _init_argparser()

    # Initialize each tool's argument parser.
    subparsers = parser.add_subparsers(
        title="COMMANDS",
        metavar="", # Remove the default metavar by setting it to an empty string. Setting it to 'None' uses a default value.
        description="The following is a set of commands you can use to select a specific tool.",
        prog="geotagx"
    )
    parents = [parser]
    initializers = [
        builder._init_argparser,
        sanitizer._init_argparser,
    ]
    for initializer in initializers:
        initializer(subparsers, parents)

    arguments = parser.parse_args(sys.argv[1:] if argv is None else argv)

    # Make sure the 'handler' argument is callable (a function or method).
    # Note: the handler is a reference set to a callable object by the tool during
    # the _init_argparser call.
    run = arguments.handler
    if not hasattr(run, "__call__"):
        parser.error("The 'handler' argument is not callable.")

    run(arguments)
    return 0
