s = input("Enter a list of numbers: ").split()

#print(s)

new_list = [int(item) for item in s]

if len(new_list) == 0:
    print("[]")
else:
# print(new_list)
    h = max(new_list)
    l = min(new_list)
    print(f"highest: {h} lowest: {l}")