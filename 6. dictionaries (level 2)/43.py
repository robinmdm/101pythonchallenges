my_dict = {
	"a": [4, 3, 2],
	"b": [5, 3, 7],
	"c": [1, 9, 10],
	"d": [3, 4, 1]
}

get_keys = list(my_dict.keys())

get_value = list(my_dict.values())

new_list = []

for i in get_value:
    if isinstance(i, list):
        i.sort()
        new_list.append(i)

print(new_list)

# new_dict = {}

# for i in get_keys:
#     for j in new_list:
#         new_dict[i] = [j]
#         new_list.remove(j)
#         break

# print(new_dict)

new_dict = dict(zip(get_keys, new_list))

print(new_dict)