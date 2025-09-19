#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    z_txt = ""
    for char in sys.argv[1]:
        if char == 'z':
            z_txt += 'z'
    if z_txt == "":
        print("none")
    else:
        print(z_txt)
else:
    print("none")
