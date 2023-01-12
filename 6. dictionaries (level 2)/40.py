li = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]

# check = [type(x) for x in li] == "list"

# check = any(isinstance(x, list) for x in li)
new_dict = {}

for list in li:
    key = list[0]
    value = list[1]
    new_dict[key] = value

print(new_dict)



# print(check)
