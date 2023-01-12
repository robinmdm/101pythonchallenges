my_dict = {"a": 15, "b": 5}

get_value = list(my_dict.values())

for value in get_value:
    if get_value.count(value) < 2:
        print("False")
        break # or exit()
    else:
        print("True")
        break



















# print(list(my_dict.values()))

# for key, value in my_dict.items():
#     get_value = list(value)
    
# if get_value in list(my_dict.values()):
#     print("True")
# else:
#     print("False")

# get_value = list(my_dict.values())



# print(result)


# print(get_value)

# for value in get_value:
#     if get_value[0] == value:
#         print("True")
#     else:
#         print("False") 

    
    # if value == [x for x in my_dict.values()]:
    #     print("True")
    # else:
    #     print("False")

