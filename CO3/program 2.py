import calculator
a=int(input("enter the value 1 "))
b=int(input("enter the value 2 "))
c=int(input("enter the choice number \n1.add,\n2.sub,\n3.product,\n4.division\n"))
if c==1:
    print("sum is ",calculator.add(a,b))
elif c==2:
    print("difference is",calculator.sub(a,b))
elif c==3:
    print("product is ",calculator.mul(a,b))
elif c==4:
    print("division is ",calculator.div(a,b))
else:
    print("invalid choice")
