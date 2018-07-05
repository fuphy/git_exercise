# task 1 Print Fibonacci series up to 100
flist_1 = [0,1]
for i in range (1,100):
    if max(flist_1)<100:
        flist_1.append(flist_1[i]+flist_1[i-1])
flist_1.pop()
print(flist_1)