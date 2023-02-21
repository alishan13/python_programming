n=int(input("enter the number"))
for i in range(0,n+1):
    for j in range(1,i):
        print("*",end=" ")
    print("\n")
for i in reversed (range(0,n)):
    for j in reversed(range(1,i)):
        print("*",end=" ")
    print("\n")
