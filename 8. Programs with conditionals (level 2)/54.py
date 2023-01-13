def year(a):
    if a % 4 == 0 and a % 100 != 0:
        print("Yes")
    else:
        print("No")

year(1912)