li = [[1,2,3], [4,5,6], [7,8,9], 10]

new_li = []

for item in li:
    if isinstance(item, list):
        for items in item:
            new_li.append(items)
    else:
        new_li.append(item)

print(new_li)