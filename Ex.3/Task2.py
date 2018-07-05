# task 2 Print the factorial of a number
input_num = int(input("please input an integer:"))
flist_2 = list (range(1,input_num+1))
output_num = 1
for j in flist_2:
    output_num *= j
print(output_num)