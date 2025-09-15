#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
else:    
    for txt in sys.argv[1:]:
        if txt[-3:] != "ism":
            print(txt + "ism")