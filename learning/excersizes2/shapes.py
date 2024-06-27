import math as m
volume=None
area=None

side2=None
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
            Shapes.area()
            print(area)
        def volume():
            Shapes.volume()
            print(volume)
        
    class Cube():
        def __init__(self,side) -> None:
            self.side=side
        def area(self):
            area = self.side **2
            return area
        def volume(self):
            volume = self.side **2
            return volume
        def print_area(self):
            pass
        def print_volume(self):
            pass
       