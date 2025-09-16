#!/usr/bin/env python3

import sys

def shrink(s):
    print(s[:8])
    
def enlarge(s):
    print(s.ljust(8, 'Z'))

if len(sys.argv) < 2:
    print("none")
else:
    for args in sys.argv[1:]:
        if len(args) > 8:
            shrink(args)
        elif len(args) < 8:
            enlarge(str(args))
        else:
            print(args)