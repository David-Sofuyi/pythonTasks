# write a function that takes in a string and gives back the lenght of the string without the len()function
# my_string = input("enter a word or string: ")

# def manual_counter(word):
#     counter = 0
#     for count in (word):
#         counter +=1
#     return counter
    
# print(manual_counter(my_string))

# def manual_counter(string):
#     counts = ()
#     for count in (string):
#         counts(word) = counts.get(string, 0) + 1
#     return counts
    
# # write a function that takes in a word and gives back the reverse of the word.

# def reverse_word(alphabet):
#     reverse = ()
#     for word in (alphabet):
#         reverse(alphabet) = reverse.get(alphabet)-1
#     return word

# reverse_word("school")
        
#write a function that takes in minutes and give the equivalent in seconds and hour.

# def convert_minutes(minutes):
#     seconds = minutes * 60
#     hours = minutes / 60
    
#     # print(f"{minutes} minutes = {seconds} seconds = {hours} hours")
#     return seconds, hours
# print(convert_minutes(300)) 

   
# write a function that takes a word and counts how many vowels are in the word.

# def count_vowels(arr):
#     vowels_present = []
#     vowels = {"a", "e", "i", "o", "u"}
#     for num in arr:
#         counts [vowels_present]= counts.get(vowels, 0) + 1
#     return counts
# print(count_vowels("pineapple"))


# write a function that take a number and return true if it prime number or false if it is not.

# def prime_number_checker(number):
#     for count in range (1, number):
#         if (number % count == 0):
#             return False
#     return True


def prime_number_checker(number):
    if (number <= 1):
        return False
    if (number <= 3):
        return True
    if (number % 2 == 0 or number % 3 == 0):
        return False
print(prime_number_checker(111))



