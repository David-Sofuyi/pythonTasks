# PSEUDOCODE:
#  Input father's current age
#  Input son's current age
#  Calculate the difference using:
#       years = abs(father_age - (2 * son_age))
#  Display the result

father_age = int(input("Enter father's current age (1 - 80): "))
son_age = int(input("Enter son's current age (1 - 80): "))

years = abs(father_age - (2 * son_age))

print("Number of years:", years)
