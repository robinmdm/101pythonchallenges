n = int(input("Enter only odd number: "))

if n % 2 == 0:
    print("Please give odd values")
else:
    middle_rows = (n + 2) // 2

    for i in range(middle_rows):
        print(" " * (middle_rows - i), "*" * (i*2 + 1))

    for i in range(middle_rows - 2, -1, -1):
        print(" " * (middle_rows - i), "*" * (i*2 + 1))
