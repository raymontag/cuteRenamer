#!/usr/bin/python

from optparse import OptionParser
from sys import exit
from textmode.textmode import textmode, os

#Parse options
parser = OptionParser("Renamer.py [options] directory")
parser.add_option("--pre", dest="prefix", default='', help="set prefix that will be placed to the left of the number")
parser.add_option("--post", dest="postfix", default='', help="set postfix that will be placed to the right of the number")
parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False, help="be chatty")
parser.add_option("-s", "--start", dest="start", default=1, help="set startnumber")
parser.add_option("-l", "--list", dest="list", default=False, help="use a list of files instead of all files in the directory")
parser.add_option("-t", "--text-mode", action="store_true", dest="text", default=False, help="start in text-mode")
parser.add_option("-g", "--graphical-mode", action="store_true", default=False, dest="graphic", help="start in graphical-mode")
(options, args) = parser.parse_args()

#Chose UI
if options.text:
    #Check last argument
    if not (len(args) == 1 and os.path.isdir(args[0])):
        parser.error("Last command-line argument must be a valid directory")
    if options.verbose:
        print "Start in text-mode"
    
    textmode(args, options)
elif options.graphic:
    print "Grapical-mode currently unsupported. Check http://gitorious.org/renamer or http://github.com/RayMontag/Renamer for updates"
    exit()
else:
    print "No UI chosen"
    exit()
