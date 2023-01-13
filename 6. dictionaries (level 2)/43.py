# s = "pramitshubhamswetharolstanpradeeprobin"

# count = 0
# new_dict = {}

# for letter in s:
#     a = s.count(letter)
#     new_dict[letter] = [a]

# print(new_dict)

names = [['PRAMIT'], ['SHUBHAM'], ['SWETHA'], ['ROLSTAN'], ['PRADEEP']]

for i in range(len(names)):
    names[i] = ''.join(reversed(names[i][0]))

for name in names:
    print(list(name))
    