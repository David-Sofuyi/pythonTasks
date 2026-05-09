# PSEUDOCODE:
#  Ask user for total bill
#  Ask if user is a member (yes/no)
#  Check conditions:
#       If bill >= 1000 and member -> 10% discount
#       If bill >= 1000 and not member -> 5% discount
#       Else -> no discount
#  Calculate final amount
#  Print discount message and final amount

total_bill = float(input("Enter total bill: "))
is_member = input("Are you a member? (yes/no): ")

if total_bill >= 1000 and is_member == "yes":
    discount = total_bill * 0.10
    final_amount = total_bill - discount
    print("10% discount applied")
elif total_bill >= 1000:
    discount = total_bill * 0.05
    final_amount = total_bill - discount
    print("5% discount applied")
else:
    discount = 0
    final_amount = total_bill
    print("No discount applied")

print("Final Amount:", final_amount)
