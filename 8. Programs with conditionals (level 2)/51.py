month = input("Enter a month: ")

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if month in months:
    i = months.index(month)

day = days[i]

print(f"{month} has: {day} days")