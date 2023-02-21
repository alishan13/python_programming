l=int(input("enter the length"))
b=int(input("enter the b"))
h=int(input("enter the h"))
ar=lambda a,b:a*b
asq=lambda a: a*a
at= lambda b,h: 0.5*b*h
print("ar",ar(l,b))
print("asq",asq(l))
print("at",at(b,h))