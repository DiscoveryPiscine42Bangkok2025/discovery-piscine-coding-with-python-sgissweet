#!/usr/bin/env python3

inp_age = int(input("Please tell me your age: "))

print(f"You are currently {inp_age} years old.")
for i in range(1, 4) :
    print(f"In {i * 10} years, you'll be {inp_age + (i * 10)} years old.")
