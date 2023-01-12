li = ["a", "b", 'a']

frequency_dict = {}

for i in li:
    if i not in frequency_dict:
        frequency_dict[i] = 1
    else:
        frequency_dict[i] = frequency_dict[i] + 1

print(frequency_dict)