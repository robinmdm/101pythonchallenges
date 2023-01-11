input_str = input("Enter a list of elements separated by space: ")
li = []
for elem in input_str.split():
    try:
        input_num = int(elem)
        li.append(input_num)
    except ValueError:
        li.append(elem)

count = 0

for number in li:
    if number > 3:
        count = count + 1
print(count)