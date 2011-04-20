'''
This file is part of the project cuteRenamer

Written by Karsten-Kai König <KKoenig@posteo.de>

Copyright (C) 2011 Karsten-Kai König <KKoenig@posteo.de>

This program is free software; you can use it under the terms of the MIT-License.
You should have received a copy of the MIT-License along with this program; 
if not check out http://www.opensource.org/licenses/mit-license.php
'''
import os
import re

'''
This function will rename all files included in "files".

The other parameters are options to configure the final file name.
'''
def rename_files(start, prefix, postfix, conserve, files):
    print "Rename files"
    
    for i in files:
        #Prepare new name
        expand = ""
        
        if conserve:
            expand = os.path.splitext(i)[1]
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
