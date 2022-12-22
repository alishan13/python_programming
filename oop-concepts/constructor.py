class Rectangle:
    def __init__(self, length, breadth, unit_cost=0):
        self.length = length
        self.breadth = breadth
        self.unit_cost = unit_cost
    
    def get_perimeter(self):
        return 2 * (self.length + self.breadth)
    
    def get_area(self):
        return self.length * self.breadth

    def calculate_cost(self):
        area = self.get_area()
        return area * self.unit_cost

field1 = Rectangle(160,120,2000)
print("Perimeter of the field :",field1.get_perimeter())
print(f"Area of the field : {field1.get_area()} cm^2 ")
print(f"Cost of the field : Rs {field1.calculate_cost()}")