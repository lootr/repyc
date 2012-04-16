#!/usr/bin/env python
import dis
import marshal
import opcode
import optparse
import struct
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
        self._magic = ''.join(struct.unpack("cccc", data[:4]))
        self._time = _time.gmtime(struct.unpack("<i", data[4:])[0])
        self._bc = marshal.load(bfile)
        if options.get('verbose'):
            print "MAGIC:", self._magic.encode('hex')
            print "TIME:",  _time.asctime(self._time)

    def show_hex(self):
        print map(ord, self._bc.co_code)
        return self

    def disassemble(self):
        i = 0
        c = map(ord, self._bc.co_code)
        while i < len(c):
          inst = c[i]
          print dis.opname[inst]
          if inst < opcode.HAVE_ARGUMENT:
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
    Repyc(*args[:2], options=vars(options)).show_hex().disassemble()
