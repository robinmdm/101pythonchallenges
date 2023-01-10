# Python program that checks if the string s contains all the letters in the alphabet (case-insensitive, so "A" should be equivalent to "a").

import string

s = input("Enter anything: ")

set_s = set(s.lower()) # making a set -> because set automatically doesnt take duplicate characters

if " " in set_s:
    set_s.remove(" ") # removes spaces
    print(set_s == set(string.ascii_lowercase))
else:
    print(set_s == set(string.ascii_lowercase))
