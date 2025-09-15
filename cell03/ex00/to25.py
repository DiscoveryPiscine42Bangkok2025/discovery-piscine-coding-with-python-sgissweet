#!/usr/bin/env python3

num_inp = int(input("Enter a number less than 25\r\n"))

if num_inp > 25 :
    print("Error")
else :
    for i in range(num_inp, 26) :
        print(f"Inside the loop, my variable is {i}")