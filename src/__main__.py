#!/usr/bin/env python
#
# The GeoTag-X command line toolkit.
#
# Copyright (c) 2016-2017 UNITAR/UNOSAT
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
def main():
    """Executes the application.
    """
    import sys
    exit_code = 0
    try:
        arguments = get_argparser().parse_args(sys.argv[1:])

        # Each tool sets a callback function when its argument parser is being
        # created. This callback allows the toolkit to execute each specific tool.
        exit_code = arguments.run(arguments)
    except Exception as e:
        _print_exception(e)
        exit_code = 1
    finally:
        sys.exit(exit_code)


def get_argparser():
    """Constructs the application's command-line argument parser.
    """
    import argparse

    parser = argparse.ArgumentParser(
        prog="geotagx",
        description="A set of tools to help administrate a GeoTag-X server.",
        add_help=False
    )
    options = parser.add_argument_group("OPTIONS")
    options.add_argument("-h", "--help", action="help", help="Display this help and exit.")
    options.add_argument("-v", "--version", action="version", help="Display version information and exit.", version=_version())

    # Initialize each tool's argument parser.
    subparsers = parser.add_subparsers(
        title="COMMANDS",
        metavar="", # Hide the default metavar by setting it to an empty string. Setting this to 'None' still displays the default value '{}'.
        description="The following is a set of commands you can use to select a specific tool.",
        prog="geotagx"
    )

    import geotagx_builder.__main__ as builder
    import geotagx_validator.__main__ as validator
    import geotagx_formatter.__main__ as formatter

    for get_argparser in [
        builder.get_argparser,
        validator.get_argparser,
        formatter.get_argparser,
    ]: get_argparser(subparsers)

    return parser


def _version():
    """Returns the project's version string."""
    from __init__ import __version__
    return "GeoTag-X Command Line Toolkit v%s, Copyright (C) 2016-2017 UNITAR/UNOSAT." % __version__


def _print_exception(exception, verbose=True):
    """Prints the specified exception information.
    If the exception does not contain a message, the stack trace will be printed
    by default.

    Args:
        exception (Exception): The exception information to print.
        verbose (bool): If set to True, the entire stack trace will be printed.
    """
    if not str(exception) or verbose:
        import traceback
        traceback.print_exc()
    else:
        print "{0}: {1}".format(exception.__class__.__name__, exception)


if __name__ == "__main__":
    main()
