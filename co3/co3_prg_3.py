from graphics.rectangle import *
from graphics.circle import *
from graphics.threed_graphics.cuboid import *
from graphics.threed_graphics.sphere import *

l=int(input("Enter the length of the rectangle : "))
b=int(input("Enter the breadth of the rectangle : "))
print("Area of Rectangle =",RectArea(l,b))
print("Perimeter of Rectangle =",RectPerimeter(l,b))

r=int(input("Enter the radius of the circle : "))
print("Area of circle =",CirArea(r))
print("Perimeter of circle =",CirPerimeter(r))

l=int(input("Enter the length of the cuboid : "))
b=int(input("Enter the breadth of the cuboid : "))
h=int(input("Enter the height of the cuboid : "))
print("Area of cuboid =",CubArea(l,b,h))
print("Perimeter of cuboid =",CubPerimeter(l,b,h))

r=int(input("Enter the radius of the sphere : "))
print("Area of sphere =",SpArea(r))
print("Perimeter of sphere =",SpPerimeter(r))


