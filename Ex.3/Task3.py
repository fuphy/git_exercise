# task 3 Define a function to return if numbers from 1 to 10 are odd or even
def OddEven (num):
    if num<1 or num>10:
        print ("please input a number in 1 to 10")
    elif (num%2) == 1:
        print ("the number is even")
    else:
        print ("the number is odd")
    return
OddEven(8)