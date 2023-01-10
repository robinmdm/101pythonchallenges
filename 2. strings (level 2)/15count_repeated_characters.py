# count repeated characters

s = "Hello"

count = 0
repeated_char = []

for char in s:
    if (s.count(char) > 1) and (char not in repeated_char):
        count = count + 1
        repeated_char.append(char)

print(count)

if (len(repeated_char) > 0):
    for char in sorted(repeated_char):
        print(char, end = " ")
else:
    print("None")    