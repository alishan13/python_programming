class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def perimeter(self):
        return(2*(self.length+self.breadth))
    def area(self):
        return(self.length*self.breadth)
    def compare(self,obj2):
        try:
            if(obj1.area()==obj2.area()):
                print("the areas are equal")
            elif(obj1.area()>obj2.area()):
                print("the area of first rectangle is larger than second")
            else:
                print("the area of second rectangle is larger than first")
        except:
            print("error occured")
a=int(input("enter the length of first"))
b=int(input("enter the breadth of first"))
a1=int(input("enter the length of second"))
b1=int(input("enter the breadth of second"))
obj1=rectangle(a,b)
obj2=rectangle(a1,b1)
print("area of first rectangle:",obj1.area())
print("area of second rectangle:",obj2.area())
obj1.compare(obj2)
 