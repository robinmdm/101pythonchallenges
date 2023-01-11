input_str_1 = input("Enter 1st list of elements separated by space: ")
input_str_2 = input("Enter 2nd list of elements separated by space: ")

list_1 = []
list_2 = []

for elem in input_str_1.split():
        input_num_1 = int(elem)
        list_1.append(input_num_1)

for elem in input_str_2.split():
        input_num_2 = int(elem)
        list_2.append(input_num_2)


final_list = [item for item in list_1 if item in list_2]

print(final_list)