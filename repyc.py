#!/usr/bin/env python
import marshal
import optparse
import os.path
import struct
import sys
import time as _time

class Repyc(object):
    """
    """
    def __init__(self, bfile, sfile=None, options=None):
        if not options:
            options = {}
        if isinstance(bfile, basestring):
            bfile = file(bfile, 'rb')
        data = bfile.read(8)
        self._magic = struct.unpack("<H", data[:2])[0]
        self._time = _time.gmtime(struct.unpack("<i", data[4:])[0])
        self._bc = marshal.load(bfile)
        if options.get('verbose'):
            print "MAGIC:", self._magic
            print "TIME:",  _time.asctime(self._time)
        self._target = None

    def find_target(self):
        base_path = os.path.join(os.path.dirname(__file__), "targets")
        for entry in os.listdir(base_path):
            p = os.path.join(base_path, entry)
            if os.path.isdir(p):
                try:
                    f = file(os.path.join(p, "magic"), 'rb')
                except IOError:
                    continue
                try:
                    magic = int(f.read())
                finally:
                    f.close()
                if magic == self._magic:
                    sys.path.append(base_path)
                    try:
                        self._target = __import__(entry, globals(), locals(), ['opcode'])
                    finally:
                        sys.path.pop()
                    break
        return self

    def show_hex(self):
        print map(ord, self._bc.co_code)
        return self

    def disassemble(self):
        i = 0
        c = map(ord, self._bc.co_code)
        while i < len(c):
          inst = c[i]
          print self._target.opcode.opname[inst]
          if inst < self._target.opcode.HAVE_ARGUMENT:
              i += 1
          else:
              i += 3
        return self

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
    (options, args) = build_parser().parse_args()
    Repyc(*args[:2], options=vars(options)).find_target()\
                                           .show_hex()\
                                           .disassemble()
