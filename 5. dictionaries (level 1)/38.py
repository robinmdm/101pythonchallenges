my_dict = {"a": 14, "b": 3, "c": 7}

get_value = list(my_dict.values())

if len(get_value) == 0:
    print("None")
else:
    for values in get_value:
        print(min(get_value))
        break