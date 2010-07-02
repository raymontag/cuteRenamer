from sys import exit
from lib.functions import rename_files, os

def textmode(args, options):
    #If list-option is chosen read it out
    if options.list and os.path.isfile(options.list):
        if options.verbose:
            print "Read filenames from %s" % options.list
        files = [i.rstrip('\n') for i in open(options.list, "r")]
    elif options.list and (os.path.isdir(options.list) or not os.path.exists(options.list)):
        print "Path to list don't exists or is not a file"
        exit()
    else:
        files = os.listdir(args[0])
    
    if options.verbose:
        print "Change directory"
        
    os.chdir(args[0])
    
    #Start Renaming
    rename_files(int(options.start), options.prefix, options.postfix, options.verbose, files)