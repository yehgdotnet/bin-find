#!/usr/bin/env python

import glob
import sys
import re


print """
----------------------------------------------
Bin Find (strings for windows) 
   - find your desired strings in binary file
 
 by Myo Soe <http://yehg.net/> 
----------------------------------------------
"""

if (len(sys.argv) < 3):
    print "Usage: bin_find.py File Keyword"
    sys.exit(0)
    

keyword = sys.argv[2]
fn = sys.argv[1]

print "Keyword: " + keyword 
print "File: " + fn
print "\n"
fh = file(fn,"rb")
c = 0
lc = 0
for l in fh:  
    le = len(re.findall( keyword,l))
    if le > 0:
        c = c + le
        if le > 1:
            print "The word '" + keyword + "' found " + str(le) + " times between offsets "  + str(lc + l.index(keyword)) + " - "  + str(lc + l.rindex(keyword))
        else:
            print "The word '" + keyword + "' found at offset "  + str(lc + l.index(keyword))
            
        
    lc = lc + len(l)  
    
    

fh.close()


if c < 1:
    print "No such word found"
else:   
    print "\nFound: " + str(c) + " times"
    
print "Bytes read: " + str(lc)
    
    
print "\n~ Done"
