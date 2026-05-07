weight = float(input("Enter weight: "))

if weight <= 2:
    print(2.5)
elif weight <= 4:
    print(4.5)
elif weight <= 10:
    print(7.5)
elif weight <= 20:
    print(10.5)
else:
    print("Cannot be shipped")
