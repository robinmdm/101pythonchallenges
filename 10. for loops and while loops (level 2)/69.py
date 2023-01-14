n = int(input("Enter n: "))

i = 1

for x in range(1, n+1):
    for y in range(1, x+1):
        print(i, end =" ")
        i = i + 1
    print()