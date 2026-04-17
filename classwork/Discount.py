 # design a program that applies tiered discounts based on a customer's total spending in a store. the greater the purchase amount, the higher the discount offered.
 
 # purchases between 1,000 and 10,000 receive a 5% discount.
 # purchases between 10,000 and #50,000 receive a 10% discount.
 # purchases avove 50, 000 receive a 20% discount.
 # Ensure the program calculates and displays the appropriate discount for the given amount.



# pseudo code
#start the program by collecting user input 
#ask for the total amount spent to calculate the percentage amount of the discount applicable 
#print out the appropriate discount.
 


user_input = ("what is the total amount you spent")
if (user_input >=1000 and user_input <= 10,000):{
    print("5% discount applicable pay")}
    discount_applied = (user_input // 0.5)
    print (discount_applied)
    
elif if (user_input >=10000 and user_input <= 50,000){
    print("10% discount applicable pay")}
    discount_applied = (user_input // 0.20)
    print (discount_applied)
    
elif (user_input >= 50,000){
    print("20% discount applicable pay")}
    discount_applied = (user_input // 0.50)
    print (discount_applied)
    
