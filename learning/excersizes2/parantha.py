# create a class on parantha to to define properties and function
"""
create a list for paranthas
    methods: consume, cooking and how many rotis
    variables: color, fillng temparature
"""

class Parantha():

    paranthas=0
    def __init__(self,color,filling,temprature) -> None:
        self.color=color
        self.filling=filling
        self.temprature=temprature
    def __str__(self) -> str:
        return f'The {self.color} parantha filled with {self.filling} at the temprature {self.temprature}'
    def cooking():
        Parantha.paranthas+=1
    def consume():
        Parantha.paranthas-=1
    def print_paranthas():
        Parantha.paranthas
def main():
    parantha_obj=Parantha(input('Color of parantha : ', input('Filling of parantha : '), input('Parantha temprature')))
    print('')
    x = True
    while x == True:
        userInput=input('Do you want to cook, eat or see how many paranthas are there or exit the program : ').lower()
        if userInput == 'cook':
            print('You have +1 parantha')
            Parantha.cooking()
        elif userInput == 'eat':
            print('You have -1 parantha')
            pass
        elif userInput == 'exit':
            exit(0)
        else:
            print('x')
    
if __name__== '__main__':
    main() 
else:
    print('.................. why arent you WORKING !!!!!!!')
