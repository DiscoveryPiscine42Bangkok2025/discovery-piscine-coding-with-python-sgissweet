#!/usr/bin/env python3

import sys

def downcase_it(txt):
    return txt.lower()

if len(sys.argv) < 2:
    print("none")
else:
    for args in sys.argv[1:]:
        print(downcase_it(args))
        