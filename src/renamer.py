#!/usr/bin/python

from optparse import OptionParser
from functions import *

parser = OptionParser("Namemangler_Python.py [options] directory")
parser.add_option("--pre",dest="prefix",default='',help="set prefix that will be placed to the left of the number")
parser.add_option("--post",dest="postfix",default='',help="set postfix that will be placed to the right of the number")
parser.add_option("-v","--verbose",action="store_true",dest="verbose",default=False,help="be chatty")
parser.add_option("-s","--start", dest="start",default=1,help="set startnumber")
parser.add_option("-l","--list",dest="list", default=False, help="use a list of files instead of all files in the directory")
(options, args) = parser.parse_args()

if len(args) == 1 and os.path.isdir(args[0]):
    if options.verbose:
        print "Change directory"
    os.chdir(args[0])
    
    files = []
    if options.list and os.path.isfile(str(options.list)):
        if options.verbose:
            print "Read filenames from %s" % options.list
        listfile = open(options.list, "r")
        for i in listfile:
            files.append(i.rstrip('\n'))
    else:
        files = os.listdir(args[0])
    rename_files(int(options.start),options.prefix,options.postfix,options.verbose,files)
else:
    parser.error("Last command-line argument must be a valid path")

