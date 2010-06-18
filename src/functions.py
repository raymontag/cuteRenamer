import os

def rename_files(start, prefix, postfix, verbose, files):
    if verbose:
        print "Rename files"
    
    for i in files:
        name = "%s%d%s" % (prefix, start, postfix)
        
        if os.path.isfile(i) and not os.path.exists(name):
            if verbose:
                print "Rename %s to %s" % (i, name)
            
            os.rename(i, name)
            start += 1
        elif os.path.isfile(i) and os.path.exists(name):
            print "Will not rename %s to %s because %s exists!" % (i, name, name)
            start += 1
        elif os.path.isdir(i):
            print "Will not rename %s to %s is a directory" % (i, name)
        elif not os.path.exists(i):
            print "%s doesn't exists" % i