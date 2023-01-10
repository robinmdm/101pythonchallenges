#Python program that prints the first and last three characters of the string s as a single string.

s = input("Enter a string: ")

if len(s) < 6:
    print("\"\"")
else:
    f = s[0:3]

    l = s[len(s)-3 : len(s)]
    t = f + l
    print(t)