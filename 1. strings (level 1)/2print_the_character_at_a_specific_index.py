#Python program that prints the character at index i in the string s.

x = input("Enter string: ")

a = int(input("Which index you want to find out?"))

if len(x) == 0:
    print("Empty String")
elif a > len(x):
    print("i is out of range")
else:
    print(x[a])