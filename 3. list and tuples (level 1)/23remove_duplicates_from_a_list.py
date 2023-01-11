input_str = input("Enter a list of elements separated by space: ")
li = []
for elem in input_str.split():
    try:
        input_num = int(elem)
        li.append(input_num)
    except ValueError:
        li.append(elem)

new_li = set(li)

final_list = list(new_li)

print(final_list)