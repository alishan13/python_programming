a=input("enter the string")
x=list(a)
temp=x[0]
x[0]=x[-1]
x[-1]=temp
print("".join(x))
#print(x)