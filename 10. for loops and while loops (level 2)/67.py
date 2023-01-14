s = input("Enter any string: ")

i = len(s)

for x in range(i-1, -1, -1):
    print(s[x], end="")


# for x in range(5,0,-1):
#     print(x)