#!/usr/bin/env python3

first_inp_num = int(input("Enter the first number:\r\n"))
sec_inp_num = int(input("Enter the second number:\r\n"))

result = first_inp_num * sec_inp_num
print(f"{first_inp_num} x {sec_inp_num} = {result}")

if result > 0 :
    print("The result is positive.")
elif result < 0 :
    print("The result is negative.")
elif result == 0 :
    print("The result is positive and negative.") 