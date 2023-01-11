li = input("Enter a list of items: ").split()
count = 0


if len(li) == 0:
    print("Empty List")
else:
    for items in li:
        print(f"{items} {count}")
        count = count + 1