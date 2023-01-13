n = int(input("Enter n: "))

factorial = 1
product = n

if n == 0:
    print(1)
else:
    for x in range(n-1, 0, -1):
        product = product * (x)
        x = x - 1
    factorial = n * product
    print(factorial)