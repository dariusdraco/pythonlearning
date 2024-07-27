import math
"""
    Create class for Circle, and Square
    ceate its data members for side and radius respectively
    provide methods of class which can be used via objects of class
    for calculation of :
        Area
        Perimiter/Circumference
"""
class Circle():
    def __init__(self,radius) -> None:
        self.radius=radius
        
    def calc_circumfrence(self) -> int:
        return math.pi * 2 * (self.radius)
    
    def calc_area(self) -> int:
        return int(math.pi*(self.radius**2))

    

class Square():
    def __init__(self,side) -> None:
        self.side=side

    def calc_perimeter(self) -> int:
        return int(self.side*4)
    
    def calc_area(self) -> int:
        return self.side ** 2
    

def main():
    circle_obj=Circle(int(input('Enter circle radius : ')))
    square_obj=Square(int(input('What is the size of the square size : ')))
    print(circle_obj.calc_area())
    print(circle_obj.calc_circumfrence())
    print(square_obj.calc_area())
    print(square_obj.calc_perimeter())

if __name__ == '__main__':
    main()