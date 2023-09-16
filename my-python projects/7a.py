import math
class Shape:
 def area(self):
  pass
class Triangle(Shape):
 def __init__(self, base, height):
  self.base = base
  self.height = height
 def area(self):
  return 0.5 * self.base * self.height

class Circle(Shape):
 def __init__(self, radius):
  self.radius = radius
 def area(self):
  return math.pi * self.radius * self.radius
class Rectangle(Shape):
 def __init__(self, width, height):
  self.width = width
  self.height = height
 def area(self):
  return self.width * self.height

choice = int(input("Choose a shape: 1. Triangle 2. Circle 3. Rectangle : "))
if choice == 1:
 base = float(input("Enter the base of the triangle: "))
 height = float(input("Enter the height of the triangle: "))
 shape = Triangle(base, height)
elif choice == 2:
 radius = float(input("Enter the radius of the circle: "))
 shape = Circle(radius)
elif choice == 3:
 width = float(input("Enter the width of the rectangle: "))
 height = float(input("Enter the height of the rectangle: "))
 shape = Rectangle(width, height)
else:
 print("Invalid choice")
 exit()
area = shape.area()
# Output
print("Area of the selected shape:", area)