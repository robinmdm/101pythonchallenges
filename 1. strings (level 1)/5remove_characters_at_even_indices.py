# Python program that prints the string s without the characters located at even indices.

s = input("Enter string: ")

if len(s) == 0:
    print("\"\"")
else:
    print(s[1::2])