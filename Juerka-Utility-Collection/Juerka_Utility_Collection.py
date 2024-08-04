#!/usr/bin/env python3
# coding: utf-8

"""This is the collection of scripts which supports Juerka.
"""

import sys
import argparse

from visualize import plot_spikes
from visualize import plot_networks

def command_visualize_spikes(args):
    plot_spikes.raster_plot(args)

def command_visualize_networks(args):
    plot_networks.network_structure_plot(args)

def main(arguments):    
    parser = argparse.ArgumentParser(prog='Juerka-utility-collection',description=__doc__)

    subparsers = parser.add_subparsers()

    parser_visualize = subparsers.add_parser('visualize_spikes', help='see `visualize_spikes -h`')
    parser_visualize.add_argument('-dirname', required=True, help='directory name which contains log files.')
    parser_visualize.add_argument('-logfile_index', required=True, help='logfile index.')
    parser_visualize.add_argument('-start_time', required=False, default=0, help='start time.')
    parser_visualize.add_argument('-silent', required=False, default=False, help='silent.')
    parser_visualize.set_defaults(handler=command_visualize_spikes)

    parser_visualize = subparsers.add_parser('visualize_networks', help='see `visualize_networks -h`')
    parser_visualize.add_argument('-dirname', required=True, help='directory name which contains weight log files.')
    parser_visualize.add_argument('-logfile_index', required=True, help='logfile index.')
    parser_visualize.add_argument('-silent', required=False, default=False, help='silent.')
    parser_visualize.set_defaults(handler=command_visualize_networks)

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
