li = int(input("How many elements you wnat to input? "))

new_li = []

for item in range(0, li):
    i = input("Enter an element: ")
    new_li.append(i)

print(new_li, end="")

if len(new_li) > 0:
    element_to_remove = input("Enter element to remove: ")
    if element_to_remove not in new_li:
        print("Not Found")
    else:
        for i in range(0, new_li.count(element_to_remove)):
            new_li.remove(element_to_remove)
else:
    print("Empty List")

try:
    modified_list = [int(item) for item in new_li if item.isdigit()]
except:
    modified_list = [(item) for item in new_li]
    
print(modified_list)



# count = 0

# for item in li:
#     if (li.count(item) > 1):
#         li.remove(item)

# print(li)