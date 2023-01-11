# x1 = float(3)
# x2 = float(1)
# y1 = float(4)
# y2 = float(3)
# z1 = float(5)
# z2 = float(5)

# formula = ((x1-x2) ** 2 +(y1-y2) ** 2 + (z1-z2) ** 2) ** 0.5
# print(formula)

list_1 = [3, 4 ,5]
list_2 = [1, 3 ,5]

sum = 0

for i in range(len(list_1)):
    x = list_2[i] - list_1[i]
    sum = sum + (x ** 2)

result = sum ** 0.5

print(result)


