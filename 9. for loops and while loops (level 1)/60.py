n = int(input("Enter n: "))

product = 1
i = 0
print(f"==== Multiplication Table of {n} ===")

for x in range(1,11):
    product = n * x
    i = i + 1
    print(f"{n} x {i} = {product}")