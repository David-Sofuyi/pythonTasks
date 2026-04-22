largest = none
while True:
    value = input("Enter any number: ")
    if value == "done":
        break
    number = int(value)
    if largest is None or number > largest:
        largest = number
print("Largest: ", largest)
