n = int(input("Enter a two-digit number: "))
tens = n // 10
units = n % 10

if tens > units:
    print("Tens greater")
elif tens < units:
    print("Units greater")
else:
    print("Equal")
