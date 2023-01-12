s = "Excellent".lower()

words = []

for letter in s:
    words.append(letter)

new_dict = {}

for letter in words:
    new_dict[letter] = words.count(letter)

print(new_dict) 
