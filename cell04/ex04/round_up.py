#!/usr/bin/env python3

inp = input("Give me a number: ")

inp = float(inp)
if inp.is_integer():
    print(int(inp))
else:
    print(int(inp) + 1)