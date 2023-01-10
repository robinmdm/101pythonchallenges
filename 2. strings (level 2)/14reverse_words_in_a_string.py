#Write a Python program that reverses the individual words in the string s and changes their capitalization. Uppercase letters should be printed in lowercase and vice versa.

s = "Python is Awesome"

# swapping upper to lower and lower to upper
swap = (s.swapcase())

# splitting words in a list
words_list = swap.split()

# new string
new_s = ""

#loop
for word in words_list:
    # inside the new string we are inserting words one by one
    new_s = new_s + " " + word[::-1]
    # removing the left most space
    new_s = new_s.lstrip()

print(new_s)