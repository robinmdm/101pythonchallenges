print("=== Welcome to your Interactive Python Calculator ===")
f_value = int(input("Please enter the first value: "))
s_value = int(input("Please enter the second value: "))
print("Great! Now enter the operation.")
print("These are the available options: ")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
print("5 - Integer Division")
print("6 - Modulo")
operation = int(input("Enter the corresponding integer: "))


if operation == 1:
    result = f_value + s_value
    op = "+"
elif operation == 2:
    result = f_value - s_value
    op = "-"    
elif operation == 3:
    result = f_value * s_value
    op = "*"    
elif operation == 4:
    result = f_value / s_value
    op = "/"    
elif operation == 5:
    result = f_value // s_value
    op = "//"    
elif operation == 6:
    result = f_value % s_value
    op = "%"

print(f"The result of {f_value} {op} {s_value} is: {result}")