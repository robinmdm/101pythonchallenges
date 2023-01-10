# Python program that prints the string s with the character curr_char replaced by the character new_char.

s = input("Give a string: ")

curr_char = input("Which character you wnat to replace? ")
new_char = input("Which character you wnat to replace with? ")

replacing = s.replace(curr_char, new_char)

print(replacing)
