class rectangle:
    def __init__(self):
        self.__length=int(input("enter the length"))
        self.__breadth=int(input("enter the breadth"))
    def __lt__(self,ob2):
        area1=self.__length * self.__breadth
        area2=ob2.__length *ob2.__breadth
        print=("the area is",area1)
        print=("the area is",area2)
        return (area1<area2)
print("enter the length and breadth of first object")
og1=rectangle()
print("enter the length and breadth of first object")
og2=rectangle()
if og1<og2:
    print("rectangle 1 is smaller")
else:
    print("rectangle 2 is smaller")