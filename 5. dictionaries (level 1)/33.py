my_dict = {}

while True:
    key = input("Enter a key (or 'done' to finish): ")
    if key == 'done':
        break
    value = input("Enter a value: ")
    my_dict[key] = value

# print(my_dict)

check_key = input("Enter a key you wnat to check: ")

if check_key in my_dict.values():
    print("True")
else:
    print("False")