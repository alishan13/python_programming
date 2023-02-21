n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(0,i+1):
        a=i*j
        if a==0:
            continue
        else:
            print(a,end="  ")
    print("\n")
    