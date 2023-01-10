# a Python program that check if a string only contains numbers.

s = input("Enter anything: ")

# isdecimal and isdigit are same

if s.isdecimal():
    print("True")
else:
    print("False")