import math as m
volume=None
area=None
class Shapes():
    class Cone():
        def __init__(self,radius,height) -> None:
            self.radius,self.height=radius,height
        def area(self):
            area=(m.pi(self.radius**2))
            return area
        def volume(self):
            volume=((1/3)*m.pi*self.radius*2*self.height)
            return volume
        def print_area():
            Shapes.Cone.area()
            print(area)
        def volume():
            Shapes.Cone.volume()
            print(volume)
    class Cube():
        def __init__(self,side) -> None:
            self.side=side
        def area(self):
            area = self.side **2
            return area
        def volume(self):
            volume = self.side **3
            return volume
        def print_area():
            Shapes.Cube.area()
            print(area)
        def print_volume():
            Shapes.Cube.volume()
            print(volume)
    class Cylinder():
         def __init__(self,radius,height) -> None:
            self.radius,self.height=radius,height
         def area(self):
            area=(m.pi(self.radius**2))
            return area
         def volume(self):
            volume=((self.radius**2)*m.pi)*self.height
            return volume
         def print_area():
            Shapes.Cylinder.area()
            print(area)
         def volume():
            Shapes.Cylinder.volume()
            print(volume)
    class Sphere():

        def __init__(self,radius) -> None:
            self.radius=radius
        def area(self):
            area=m.pi*((self.radius)**2)
            return area
        def volume(self):
            area=m.pi*((self.radius)**3)*(4/3)
            return volume
        def print_area():
            Shapes.Sphere.area()
            print(area)
        def print_volume():
            Shapes.Sphere.volume()
            print(volume)
    class Cuboid():
        def __init__(self,side,side2,height) -> None:
            self.side=side
            self.side2=side2
            self.height=height
        def area(self):
            area = self.side*self.side2
            return area
        def volume(self):
            volume = self.side*self.side2*self.height
            return volume
        def print_area():
            Shapes.Cube.area()
            print(area)
        def print_volume():
            Shapes.Cube.volume()
            print(volume)
def print_manual():
    print('''
This is a text simulator to create shapes and calculate area and volume
here are the commands :
        create (shapes include cone,cube,cylinder,sphere,cuboid) : asks for shape, enter info
        area show : prints area
        volume show : prints volume
        another : asks for new shape
        thanks : exits
''')
def input_taking_function(user_input):
    if user_input != 'exit':
        if user_input == 'create':

    else:
        exit(0)
if __name__ == "__main__":
    while True:
        input_taking_function(input(' : '))