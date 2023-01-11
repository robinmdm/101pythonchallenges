# a Python program that check if a string only contains numbers.

s = input("Enter anything: ")

# isdecimal and isdigit are same

if s.isdigit():
    print("True")
elif len(s) == 0:
    print("\"\"")
else:
    str = None
    for char in s:
        if char.isdigit():
            str = True
            print(str)
            exit()
    str = False
    print(str)