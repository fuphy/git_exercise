# Task 4 Define a function to check if a given string is a palidrome
def isPalindrome (str):
    if str == str[::-1]:
        print ('palindrome')
    else:
        print ('no palindrome')
    
isPalindrome('madam')