# Write a Python program that checks if the string s ends with the sequence of characters denoted by the variable prefix.

s = input("Enter anything: ")
check_suffix = input("Give your suffix: ")

if s.endswith(check_suffix):
    print("True")
else:
    print("False")