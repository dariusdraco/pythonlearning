class Chair:
    _total_chairs = 0

    def show_total_chairs() -> int:
        return Chair._total_chairs
    
    """
        This is a sample parent Chair class
        with attributes as : 
            size : big, medium, small, x-large
            color : gree, blue, black, red, brown , yellow
            num_of_legs : any integer
    """
    def __init__(self, size, color, no_of_legs) -> None:
        self._size = size
        self._color = color
        self._legs = no_of_legs
        Chair._total_chairs += 1
    
    def add_legs(self, num_to_add) -> None:
        self._legs += num_to_add
            
    def change_color(self, new_color) -> None:
        """
        Change the color or chair, passed as new_color param
        """
        self._color = new_color
 
    def __str__(self) -> str:
        return f"Chair of color {self._color} with {self._legs} legs"
    
    def __del__(self) -> None:
        print(f"Destroying the chair {type(self)}, {hex(id(self))}")


def main() -> None:
    chair1 = Chair('big','green',4)
    print(chair1)   
    chair1.change_color('yellow')
    print(chair1)
    print(vars(chair1))
    



if __name__ == "__main__":
    main()