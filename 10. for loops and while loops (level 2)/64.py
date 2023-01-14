n = int(input("Enter a number: "))

if n == 0 or n == 1:
    print("Not Prime")
else:
    for x in range(2, n):
        if n % x == 0:
            print("Not Prime")
            exit()
    print("Prime")
    