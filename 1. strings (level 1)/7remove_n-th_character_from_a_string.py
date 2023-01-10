# Python program that prints the string s without the character at index n.

s = input("Enter the string: ")

i = int(input("Which index you want to remove? "))

before_i = s[:i]
after_i = s[i+1:]

if len(s) == 0:
    print("\"\"")
else:
    print(before_i + after_i)