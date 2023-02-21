a=input("first string")
b=input("second string")
c=a[0]
a=a.replace(a[0],b[0])
b=b.replace(b[0],c)
print(a," ",b)