n = int(input("Enter n: "))

i = 65

for x in range(1, n+1):
    for y in range(1, x+1):
        print(chr(i+1), end = "")
        i = i+1
    print()