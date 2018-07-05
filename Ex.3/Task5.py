# Task 5 Define a function to check if numbers between 1-20 are prime or not
def isPrime (num2):
    if num2<1 or num2>20:
        print ("please input a number in 1 to 20")
    else:
        tmpl=[]
        for x in range (2,num2):
            tmpl.append(num2%x)
        if 0 in tmpl:
            print ("not prime number")
        else:
            print ("prime number")
    return
isPrime(4)