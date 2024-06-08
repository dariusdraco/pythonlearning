import pprint 
# dictionary and variable creation
paranthas,paranthas_name_list,user_input={},[],''
# defining class and functions
class ParanthaClass():
    paranthaCount=0
    def __init__(self,color,filling,temprature) -> None:
        self.color = color
        self.filling = filling
        self.temprature = temprature
    def cook():
        ParanthaClass.paranthaCount+=1
        print('One parantha cooked.')
    def eat():
        ParanthaClass.paranthaCount-=1
        print('One parantha eaten.')
    def parantha_print():
        print(ParanthaClass.paranthaCount)
def print_inst():
    print(f'''
Hi, this is the instruction manual. this is a program designed to teach the developer about
how to use functions and classes by making a program based on paranthas, an indian dish origionating
from 1526 AD frequently enjoyed by  panjab.

Here are a few different functions:
help (gives you the commands)
exit (quits program) 
add (this creates a new variaty of paranthas)
cook (entering this will provide you with a variety of paranthas you have made, enter number)
eat (entering this will provide you with a variety of paranthas you have made, enter number)
show (shows a singualar variaty of parantha)

    ''')
def main():
     while True:
        user_input=input(' : ')
        if user_input != 'exit':
            if user_input == 'help':
                print_inst()
            elif user_input == 'add':
                x = ParanthaClass(input('Enter parantha colour : '), input('Enter parantha filling : '),input('ENter parantha temprature : '))
                paranthas_name_list.append(x.filling)
                paranthas[{f'{x.filling}':{
                    'color':x.color,
                    'filling':x.filling,
                    'temprature':x.temprature
                }}]
            elif user_input == 'show':
                pprint.pprint(paranthas_name_list)
            elif user_input == 'cook':
                pprint.pprint(paranthas_name_list)
                user_input=input(' : ')
                for i in len(paranthas_name_list):
                    if user_input == paranthas_name_list[i]:
                         paranthas_name_list[i].paranthacount   
        else:
            print('')
            print('')
            print('Yipee kayak other buckets !! - charles boyle')
            exit(0)
#running the program
if __name__=='__main__':
    print_inst()
    main()