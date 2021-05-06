# Made by Snehashish Laskar!
# Made on 18-03-2021
# Developer contact: snehashish.laskar@gmail.com
# This is a mensuration calculator

""" 
    Intsructions:
    -> Please read the notes below before using this 
"""

# Create a class where all the area related functions are defined
class Area:

    def __init__(self):
        pass

    # Function to find the area of square
    def square(self, side):
        self.area = side*side 
        print(f"area of square = {self.area}")

    def rectangle(self, length, breadth):
        self.area = length*breadth
        print(f"area of rectangle = {self.area}")

    def triangle(self, height, base):
        self.area = (height*base)/2
        print(f"area of triangle = {self.area}")

    def parallelogram(self, height, breadth):
        self.area = breadth*height
        print(f"area of parallelogram = {self.area}")

    def circle(self, radius):
        self.area = 3.14*(radius**2)
        print(f"area of circle = {self.area}")
    
    def rohmbus(self, diagonal1, diagonal2):
        self.area = (diagonal2*diagonal1)/2
        print(f"area of rohmbus = {self.area}")

    def trapezium(self, side1, side2, height):
        self.area = (height/2)*(side1+side2)
        print(f"area of trapezium = {self.area}")


class Perimeter:

    def __init__(self):
        pass

    def square(self, side):
        self.perimeter =  4*side
        print(f"Perimeter of square = {self.perimeter}")

    def rectangle(self, length, breadth):
        self.perimeter =  2*(length + breadth)
        print(f"Perimeter of rectangle = {self.perimeter}")

    def triangle(self, side1, side2, base):
        self.perimeter =  side1 + side2 + base
        print(f"Perimeter of triangle = {self.perimeter}")

    def parallelogram(self, length, breadth):
        self.perimeter =  2*(length + breadth)
        print(f"Perimeter of parallelogram = {self.perimeter}")

    def circumference_of_circle(self, radius):
        self.circumference = 2*(3.14*radius) 
        print(f"Circumference of circle = {self.circumference}")


class Volume:

    def __init__(self):
        pass

    def cube(self, side):
        self.volume = side**3 
        print(f"Volume of cube = {self.volume}")

    def cuboid(self, length, breadth):
        self.volume = height*base*length
        print(f"Volume of cuboid = {self.volume}")

    def cylinder(self, height, radius):
        self.volume = (3.14*(radius**2))*height
        print(f"Volume of cylinder = {self.volume}")

class Surface_area:

    def __init__(self):
        pass

    def cube(self, side):
        self.surface_area = 6*(side**2)
        print(f"Surface area of cube = {self.surface_area}")

    def cuboid(self, length, breadth):
        self.surface_area =6*(length*breadth)
        print(f"Surface area of cuboid = {self.surface_area}")

class Lateral_Surface:

    def __init__(self):
        pass

    def Cube(self, side):
        self.surface_area = 4*(side*side)
        print(f"Lateral Surface of cube= {self.surface_area}")

    def Cuboid(self, length, breadth, height):
        self.surface_area = height*(2*(length + breadth))
        print(f"Lateral Surface area of cuboid = {self.surface_area}")

    
Area = Area()
Perimeter = Perimeter()
Volume = Volume()
Surface_Area = Surface_area()
Lateral_Surface_Area = Lateral_Surface()