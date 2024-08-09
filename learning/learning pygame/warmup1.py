import os
class Vehicle():

    def __init__(self,name,model,color,OrigionCountry,owner) -> None:
        self.name=name
        self.model=model
        self.color=color
        self.OrigionCountry=OrigionCountry
        self.owner=owner
        
    def __str__(self) -> str:
        os.system('clear')
        print(f'''
        The {self.color} {self.name} {self.model}, was made in {self.OrigionCountry}, and currently owned by {self.owner}
        ''')
        

vehicleObject1=Vehicle(input('Name of the vehicle : '),
    input('Model of the vehicle : '),
    input('Color of the vehicle : '),
    input('Vehicles country of origion : '),
    input('Owner of the vehicle : '))

if __name__ == '__main__':
    vehicleObject1.__str__()




