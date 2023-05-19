import math
# --- Superclass ---
class shapes:
    def __init__(self,length,width=0,height=0):
        self.name = None 
        self.length = length
        self.width = width
        self.height = height
        self.volume = 0
    def get_name(self):
        return self.name
    def get_length(self):
        return self.length
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def get_volume(self):
        return self.volume
 
# --- Sub classes ---    
class Rectangle(shapes):
    def calculate_volume(self):
        self.name = self.__class__.__name__
        self.volume = self.length * self.width * self.height
class Square(shapes):
    def calculate_volume(self):
        self.name = self.__class__.__name__
        self.volume = self.length * self.length * self.length
class Sphere(shapes):
    def calculate_volume(self):
        self.name = self.__class__.__name__
        self.volume = (4/3) * math.pi * self.length ** 3

# --- main ---          
rectangle = Rectangle(5,10,15)
rectangle.calculate_volume()

print(f"Name:{rectangle.get_name()}",
f"Length:{rectangle.get_length()}",
f"Width:{rectangle.get_width()}",
f"Height:{rectangle.get_height()}",
f"Volume:{rectangle.get_volume()}")



sphere = Sphere(5)
sphere.calculate_volume()

print(f"Name:{sphere.get_name()}",
f"Length:{sphere.get_length()}",
f"Volume:{sphere.get_volume()}")



square_list = [5,10,15,20,25]
for i in square_list:
    square = Square(i)
    square.calculate_volume()

    print(f"Name:{square.get_name()}",
    f"Length:{square.get_length()}",
    f"Volume:{square.get_volume()}")
