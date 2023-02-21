from math import sqrt
n=int(input("enter the final number"))
for i in range(1000,n):
    if sqrt(i)==int (sqrt(i)) and i%2==0:
        print(i)