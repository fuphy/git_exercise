# task 1 Print Fibonacci series up to 100
flist_1 = [0,1]
for i in range (1,100):
    if max(flist_1)<100:
        flist_1.append(flist_1[i]+flist_1[i-1])
flist_1.pop()
print(flist_1)

# task 2 Print the factorial of a number
input_num = int(input("please input an integer:"))
flist_2 = list (range(1,input_num+1))
output_num = 1
for j in flist_2:
    output_num *= j
print(output_num)

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

# Task 4 Define a function to check if a given string is a palidrome
def isPalindrome (str):
    if str == str[::-1]:
        print ('palindrome')
    else:
        print ('no palindrome')
    
isPalindrome('madam')

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






