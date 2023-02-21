m=int(input("enter the number of elements"))
l=[]
for i in range(m):
    n=int(input("enter the number"))
    if n>100:
        l.append("over")
    else:
        l.append(n)
print(l)