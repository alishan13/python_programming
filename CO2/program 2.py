nterms=int(input("enter the number"))
n1,n2=0,1
count=0
if nterms==1:
    print("fibonacci is")
    print(n1)
else:
    print("fibonacci sequence ")
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
