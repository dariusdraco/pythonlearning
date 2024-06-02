# make phone class and add atribute like phone number, model and company
class Phone():
    # storage dictionary for all phones with key as 
    # mobile number
    phones={}
    def __init__(self,number,model,company):
        self.phone_number=number
        self.model=model
        self.company=company

    # define string representaiton of object
    def __str__(self) -> str:
        return f'model : {self.model}, company : {self.company}'

    # saves a new phone in dictionary and put number as key
    def adding_phone(inputPhone) -> None:
        dic_key = inputPhone.phone_number
        dic_val = inputPhone
        Phone.phones[dic_key] = dic_val

def main():
    cont = True
    while cont is True:
        print("Input the details of phone :")
        phone_num = int(input(" Phone Number : "))
        phone_model = str(input("What is your phone model : "))
        phone_company = str(input("Which brand your phone is from : "))
        phone1 = Phone(phone_num,phone_model,phone_company)
        phone1_str = phone1.__str__()
        Phone.adding_phone(phone1)
        choice = str(input("Do you want to enter anohter phone? (y/n)"))
        if(choice.lower() == 'y'):
            cont = True
        else:
            cont = False
    
    try:
        find_num = int(input("Enter the number to search : "))
    except:
        print('That is the wrong input, put only a number bro : ')
        find_num = int(input("Enter the number to search : "))
   

    if Phone.phones.keys().__contains__(find_num):
        print(Phone.phones[find_num])
    else:
        print('Sorry, not found in our system')

if __name__ == "__main__":
    main()