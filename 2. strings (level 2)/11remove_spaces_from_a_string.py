# Write a Python program that prints a copy of the string s without any spaces.


# option 1

s = "hey robin"
new_s = ""

for char in s:
    if char != " ":
        new_s = new_s + char

print(new_s)

#option 2

s = input("Enter anything: ")

new_string = s.replace(" ", "")

print(new_string)