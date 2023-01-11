# Write a Python program that multiplies all the items in a list by the value of the variable factor.
# nn_li = input("Enter a list of elements: ").split()

# multiply = int(input("Multiply with: "))
# print(nn_li)

# try:
#     modified_list = [int(item) for item in nn_li if item.isdigit() == True]
#     print(modified_list)

#     new_list = [(item * multiply) for item in modified_list]
# except:
#     new_list = [(item * multiply) for item in nn_li]
    
# print(new_list)

# nn_li = input("Enter a list of elements: ").split()

# multiply = int(input("Multiply with: "))
# new_list = []

# for item in nn_li:
#     try:
#         new_list.append(int(item) * multiply)
#     except ValueError:
#         new_list.append(item * multiply)

# print(new_list)


input_type = input("Enter type of input(n for number and s for string) :")
nn_li = input("Enter a list of elements: ").split()
multiply = int(input("Enter multiply value: "))

if input_type == 'n':
    new_list = [int(item)*multiply for item in nn_li if item.isdigit()]
else:
    new_list = [item*multiply for item in nn_li]

print(new_list)
