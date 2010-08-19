import os
import re

#A function to rename the files
def rename_files(start, prefix, postfix, conserve, files):
    print "Rename files"
    
    for i in files:
        #Prepare new name
        expand = ""
        
        if conserve:
            expand = re.search(r"(\..*)$", i)
            if not expand == None:
                expand = expand.group(0)
            else:
                expand = ""
            
            print "Conserve expand %s" % expand
        
        name = "%s%d%s%s" % (prefix, start, postfix, expand)
        
        #Rename the file!
        if os.path.isfile(i) and not os.path.exists(name):
            print "Rename %s to %s" % (i, name)
            
            os.rename(i, name)
            start += 1
        elif os.path.isfile(i) and os.path.exists(name):
            print "Will not rename %s to %s because %s exists!" % (i, name, name)
            start += 1
        elif os.path.isdir(i):
            print "Will not rename %s to %s, 'cause it's a directory" % (i, name)
        elif (not os.path.exists(i)) and (not i == ""):
            print "%s doesn't exists" % i
