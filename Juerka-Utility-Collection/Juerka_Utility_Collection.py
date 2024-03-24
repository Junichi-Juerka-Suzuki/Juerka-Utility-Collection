#!/usr/bin/env python3
# coding: utf-8

"""This is the collection of scripts which supports Juerka.
"""

import sys
import argparse

from visualize import plot_spikes

def command_visualize(args):
    plot_spikes.raster_plot(args)

def main(arguments):

    parser = argparse.ArgumentParser(prog='Juerka-utility-collection',description=__doc__)

    subparsers = parser.add_subparsers()

    parser_visualize = subparsers.add_parser('visualize', help='see `visualize -h`')
    parser_visualize.add_argument('-dirname', required=True, help='directory name which contains log files.')
    parser_visualize.add_argument('-logfile_index', required=True, help='logfile index.')
    parser_visualize.set_defaults(handler=command_visualize)

    args = parser.parse_args(arguments)

    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()

if __name__ == '__main__':

    return_value = 0

    try:
        main(sys.argv[1:])
    except Exception as e:
        print(e)
        return_value = 1

    sys.exit(return_value)