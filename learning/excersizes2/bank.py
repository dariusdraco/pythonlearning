balance_difference=0
dictionary_of_bank_acounts = {}
bank_acount_number_lists=[]
bank_acount_var_obj = None
user_string_input = ''
class BankAcountClass():

    currentBankAcountNumberId='0000'

    def __init__(self,balance,bank_acount_name,bank_acount_number) -> None:
        self.balance=balance
        self.bank_acount_name=bank_acount_name
        self.bank_acount_number = bank_acount_number
    
    def add(): 
        temporary_bank_acount_name=input('Enter name of bank acount : ')
        BankAcountClass.currentBankAcountNumberId=int(BankAcountClass.currentBankAcountNumberId)
        BankAcountClass.currentBankAcountNumberId+=1
        BankAcountClass.currentBankAcountNumberId=str(BankAcountClass.currentBankAcountNumberId)
        while len(BankAcountClass.currentBankAcountNumberId) != 4:
            BankAcountClass.currentBankAcountNumberId = '0' + BankAcountClass.currentBankAcountNumberId
        user_string_input = float(input('Enter inital deposit : '))
        dictionary_of_bank_acounts[temporary_bank_acount_name]=BankAcountClass(user_string_input, temporary_bank_acount_name,BankAcountClass.currentBankAcountNumberId)
        verify_account = dictionary_of_bank_acounts[temporary_bank_acount_name]
        if verify_account != None:
            print(f"Account added : {verify_account}")
        else:
            print(f"Account could not be opened")
    
    def deposit(self):
        balance_difference=float(input('How much do you want to deposit : '))
        self.balance+=balance_difference
        print('amount deposited ...')
        print(f'before deposit : {self.balance-balance_difference}, after deposit {self.balance}')

    def withdraw(self):
        balance_difference=float(input('How much do you want to withdraw : '))
        self.balance-=balance_difference
        print(f'before withdrawal : {self.balance+balance_difference}, after withdrawal {self.balance}')

    def deposit_from_bank():
        acct_2_deposit = str(input('What bank acount do you want to deposit from : '))
        bank_acount_var_obj = dictionary_of_bank_acounts[acct_2_deposit]
        bank_acount_var_obj.deposit()
    
    def withdraw_from_bank():
        acct_2_deposit = str(input('What bank acount do you want to withdraw from : '))
        bank_acount_var_obj = dictionary_of_bank_acounts[acct_2_deposit]
        bank_acount_var_obj.withdraw()
    
    
    def showacct(self):
        print(f'bank acount name : {self.balance}')
        print(f'bank acount number : {self.bank_acount_number}')
        print(f'bank acount balance : {self.bank_acount_name}')

    def show():
        account_num = input('What bank acount do you want to deposit from : ')
        bank_acount_var_obj = dictionary_of_bank_acounts.get(account_num)
        if bank_acount_var_obj:
            bank_acount_var_obj.showacct()
        else:
            print(f'Could not find the account with number {account_num}')

    def __str__(self) -> str:
        return f"{self.bank_acount_name}"


def manual():
    print('''
Hello this is a bank acount text simulator in which you can create, withdraw, deposit
see and exit the program in general, the commands are : 
          - exit
          - add
          - withdraw
          - deposit
          - show
''')

def user_input_function(user_input_var):
    if user_input_var != 'exit':
        if user_input_var == 'add':
            BankAcountClass.add()
        if user_input_var == 'deposit':
            BankAcountClass.deposit_from_bank()
        if user_input_var == 'withdraw':
            BankAcountClass.withdraw_from_bank()
        if user_input_var == 'show':
            BankAcountClass.show()
    else:
        exit(0)
if __name__ == '__main__':
    manual()
    while True:
        user_input_function(input('''
                                  
    :   '''))