#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    sys.exit(1)
    
inp = input("What was the parameter? ")
if sys.argv[1] != inp:
    print("Nope, sorry...")
else:
    print("Good job!")