import calculator as c
a= int(input('Enter the first number : '))
b=int(input('Enter the second number : '))

choice=int(input('Enter your choice 1.add 2.substract 3.multiply 4.divide : '))

if choice == 1:
    print(c.sum(a,b))

elif choice == 2:
    print(c.sub(a,b))

elif choice == 3:
    print(c.mul(a,b))

elif choice == 4:
    print(c.div(a,b))
