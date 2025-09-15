#!/usr/bin/env python3

import sys, re

if len(sys.argv) < 3:
    print("none")
elif len(sys.argv) == 3:
    key = sys.argv[1]
    search_str = sys.argv[2]
    match = re.findall(key, search_str)
    print(len(match))
else:
    sys.exit(1)