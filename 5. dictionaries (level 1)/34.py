# my_dict = {}

# while True:
#     key = input("Enter a key (or 'done' to finish): ")
#     if key == 'done':
#         break
#     value = input("Enter a value: ")
#     my_dict[key] = value

di = {"January": 45, "February": 56, "March": 67}

di_1 = {"January": 67}

# if list(di_1) not in list(di):
#     di.update(di_1)

print(di)

for key, value in di_1.items():
    if key not in di:
        di[key] = value

print(di)

# if di_1.keys() - di.keys():
#     d2 = di.update(di_1)
# else:
#     d2 = di_1

# print(d2)


# for key not in di:
#     if key not in list(di_1):
#         di.update(di_1)
#     else:
#         di
# print(di)