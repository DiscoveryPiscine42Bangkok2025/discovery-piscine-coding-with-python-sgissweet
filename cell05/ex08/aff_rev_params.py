#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
else:
    args = sys.argv[1:]
    args.reverse()
    for i in args:
        print(i)