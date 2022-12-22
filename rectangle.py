class rectangle:
    def __init__(self , length,breadth):
        self.length=length
        self.breadth=breadth
    def get_perimeter(self):
        return 2*(self.length + self.breadth)
    def get_area(self):
        return self.length*self.breadth

    def compare(self,o2):
        try:
            if obj1.get_area()==obj2.get_area():
                print("both areas are equal")
            elif obj1.get_area()>obj2.get_area():
                print("area of first rectangle is greater than second rectangle")
            elif obj1.get_area()<obj2.get_area():
                print("area of first rectangle is smaller than second rectangle")
        except:
            print("An error has raised")

obj1=rectangle(10,20)
obj2=rectangle(12,24)
print(obj1.get_area())
print(obj2.get_area())
obj1.compare(obj2)