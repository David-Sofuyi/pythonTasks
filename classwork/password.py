 # creae a program that evaluates the strenght of a users password based on its lenght. the program should prompt the user to enter a password, analyze its lenght and classify it into one of four categories: very week, weak, strong or very strong.


# pseudo code
#request for the password from the user
#count the lenght of the password
#print the result






user_input =(input ("Enter your password: "))
lenght_checker =len(user_input)

if(lenght_checker < 8):
    print("very week")
elif(lenght_checker == 8):
    print("week")
elif(lenght_checker > 8 and lenght_checker <= 16):
    print("strong")
elif(lenght_checker > 16):
    print("very strong")    
    
    
    
    
    
    






















  
   
