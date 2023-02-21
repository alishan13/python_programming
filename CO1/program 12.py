a=[]
n=int(input("enter the number"))
for i in range (0,n):
    b=input("enter the color name")
    a.append(b)
print(a,sep=",")
print(a[0],a[-1])