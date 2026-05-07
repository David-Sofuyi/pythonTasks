temprature = int(input("Enter temperature: "))

if temprature < 0:
    print("Freezing")
elif temprature <= 15:
    print("Cold")
elif temprature <= 25:
    print("Warm")
else:
    print("Hot")
