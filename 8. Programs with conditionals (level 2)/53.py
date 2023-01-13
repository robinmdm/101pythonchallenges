def find_quad(a,b,c):
    d = (b ** 2) - (4 * a * c)

    if d < 0:
        print("Complex roots")
    elif d == 0:
        result = (-b / (2 * a))
        print(result)
    else:
        p_result = ((-b + (d) ** 0.5) / (2 * a))
        n_result = ((-b - (d) ** 0.5) / (2 * a))
        print(f"{p_result} {n_result}")

find_quad(2,5,-3)
