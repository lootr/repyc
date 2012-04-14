#!/usr/bin/env python

import optparse

def build_parser():
    """
    Create the argument parser
    """
    parser = optparse.OptionParser()
    parser.add_option("-v", "--verbose", action="store_true",
                      dest="verbose", default=False,
                      help="print disassembling information")
    return parser

if __name__ == '__main__':
    (option, args) = build_parser().parse_args()
