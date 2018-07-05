# Task 1
# 1.1 

for num in range (1,11):
    print (num)

x=0
while x <=10:
    print (x)
    x=x+1

# 1.2
for y in range (5,-6,-1):
    print (y)


z=5
while z >= -5:
    print (z)
    z=z-1

# Task 2
num_l = list (range (-10,11))

print (num_l)
for a in num_l:
    print (a)

# Task 3
for b in reversed (num_l):
    print (b)

for c in num_l[::-1]:
    print (c)

# print out the count down of list length
# for d in range(len(num_l)-1,-1,-1):
    # print(d)


# Task 4 create a dictionary of 5 items and print the key and value using for loop 
dict_1 = {'name':'ankur','university':'TUM','degree':'master','hobby':'cooking','living':'munich'}

for key in dict_1.keys():
    print (key)
for value in dict_1.values():
    print (value)

# Task 5
celsius = float (input ('Please input celsius:'))
#celsius = round(celsius, 2)
fahrenheit = (celsius * 1.8)+32
#print ('%.2f Celsius to Fahrenheit is %.2f' % (celsius,fahrenheit))
print (round(fahrenheit, 2))
