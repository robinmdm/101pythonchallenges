input_str = input("Enter a list of elements separated by space: ")
li = []
for elem in input_str.split():
    input_num = int(elem)
    li.append(input_num)

li.sort()

if len(li) < 2:
    print("None")
elif len(li) == 0:
    print("None")
else:
    second_largest = li[len(li) - 2]
    print(second_largest)