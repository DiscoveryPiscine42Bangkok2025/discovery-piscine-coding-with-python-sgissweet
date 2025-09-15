#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
else:    
    start = sys.argv[1]
    end = sys.argv[2]
    arr = []
    for i in range(int(start), int(end) + 1):
        arr.append(i)
    print(arr)