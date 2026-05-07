month = int(input("Enter month 1-12: "))
year = int(input("Enter year: "))

leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31
elif month in [4, 6, 9, 11]:
    days = 30
elif month == 2:
    days = 29 if leap else 28
else:
    days = -1

print("Invalid month" if days == -1 else days)
