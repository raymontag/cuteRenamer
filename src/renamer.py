#!/usr/bin/python

import sys.exit
from optparse import OptionParser
from functions import *

parser = OptionParser("Renamer.py [options] directory")
parser.add_option("--pre", dest="prefix", default='', help="set prefix that will be placed to the left of the number")
parser.add_option("--post", dest="postfix", default='', help="set postfix that will be placed to the right of the number")
parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False, help="be chatty")
parser.add_option("-s", "--start", dest="start", default=1, help="set startnumber")
(options, args) = parser.parse_args()

if len(args) == 1:
    if options.verbose:
        print "Change directory"
    os.chdir(args[0])
    
    if os.path.isfile(args[0]):
        if options.verbose:
            print "Read filenames from %s" % args[0]
        files = [i.rstrip('\n') for i in open(args[0],"r")]
    elif os.path.isdir(args[0]):
        files = os.listdir(args[0])
    elif not os.path.exists(args[0]):
        print "File or directory don't exists!"
        sys.exit()
        
    rename_files(int(options.start), options.prefix, options.postfix, options.verbose, files)
else:
    parser.error("Last command-line argument must be a valid path or a file which contain filenames")

