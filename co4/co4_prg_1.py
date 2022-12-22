class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def get_perimeter(self):
        return 2 * (self.length + self.breadth)
    
    def get_area(self):
        return self.length * self.breadth
    def compare(self,field):
        try:
            if self.get_area() > field.get_area():
                print("Field1 is the largest")
            elif self.get_area() == field.get_area():
                print("Both the field is of same area")
            else:
                print("Field2 is the largest")
        except:
            print("Cant compare")

field1 = Rectangle(160,120)
field2 = Rectangle(180,20)
print("Perimeter of the field1 :",field1.get_perimeter())
print(f"Area of the field1 : {field1.get_area()} cm^2 ")
print("Perimeter of the field2 :",field2.get_perimeter())
print(f"Area of the field2 : {field2.get_area()} cm^2 ")
field1.compare(field2)