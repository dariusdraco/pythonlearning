''''
Enter command in the input

'''
class ParanthaClass():
    def __init__(self,p_amount,cook,eat,filling) -> None:
        self.p_amount = int(p_amount)
        self.filling = filling
        self.cook=cook
        self.eat=eat
    def show_p(self):
        print(f'parantha amount = {self.p_amount}')
        print(f'filling = {self.filling}')
    def eat_p(self):
        self.p_amount-=1
        print(f'A parantha eaten ...')
    def cook_p(self):
        self.p_amount+=1
        print(f'A parantha cooked ...')

        
def print_manual():
    print(f'''
Hello, this is a text simulator on eating, cooking and creating different varieties of paranthas
here are the different instructions you have at your control.
          - help ( gives you into and list of instructions )
          - add ( creates new variant of paranthas)
          - cook ( makes you cook a parantha of any variant)
          - eat ( makes you cook a parantha of any variant)
          - show ( shows parantha filling and how much paranthas are there )
Enter the following commands in the input
''')
    
def user_input(user_input_var,parantha_types,key_num):
    key_num=0
    if user_input_var != 'exit':
        if user_input_var == 'help':
            print_manual()
        if user_input_var == 'add':
            key_num+=1
            parantha_types[str(key_num)]=ParanthaClass(0,input(''))
        if user_input_var == 'show':
            pass
    else:
        exit(0)

def start_file_program():
    print_manual()
    while True:
        user_input(input(f'''                         
enter command : '''),{},0)

# Main execution of program
if __name__ == "__main__":
    start_file_program()