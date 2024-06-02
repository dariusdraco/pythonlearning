# Write a program to create a class called Cookie 
# with attributes flavour, size and color, shape. 
"""
    flavour : butter, oats, choco, mint, vanilla
    color : yellow, brown, black, green, white
    shape : circle, triangle
    size : small, medium, large

"""
# Create multiple objects of this class.
class Cookie():
    def __init__(self,name, color,shape) -> None:
        self.name = name
        self.color=color
        self.shape=shape
        
    def __str__(self) -> str:
        return f'cookie {self.name} '
    

cookie_list = list()
for i in range(3):
    cookie_list.append(Cookie(i+1,input("Enter Color: "),input("Enter shape: ")))
    print(cookie_list[i])

enter_list = [_.name for _ in cookie_list]
print(enter_list)