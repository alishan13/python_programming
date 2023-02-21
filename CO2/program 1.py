def calc_factorial(x):
    if x==1:
        return 1;
    else:
        return(x*calc_factorial(x-1))
n=int(input("enter the number"))
if n>0:
    print("factorial is:",calc_factorial(n))
elif n==0:
    print( "the factorial is 1")
    
else:
    print("factorial doesnt exist")