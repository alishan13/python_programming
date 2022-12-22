# Build-in Errors
try:
    a = int(input("Enter a (>10) :"))
    b = int(input("Enter b :"))
    if a < 10:
        raise Exception
    c = a/b
except ValueError as e:
    print("Enter an integer value")
except ZeroDivisionError as e:
    b=1
    c=a/b
    print(c)
except:
    print("value of a cannot be lessthan 10")
else:
    print(a/b)
finally:
    print("Program ended...")


