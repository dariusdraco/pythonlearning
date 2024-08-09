def count_lower_upper(strng,strngLen):
    strngLen=len(strng)
    capcount,lowcount=0,0
    for i in range(strngLen):
        if strng[i] == " ":
            pass
        elif strng[i].isalpha() != True:
            print(f'this very text is so powerfull that it destrupted the laws of physics')
            exit(0)
        elif strng[i] == strng[i].upper():
            capcount+=1
        elif strng[i] == strng[i].lower():
            lowcount+=1
    print(f'There are {capcount} capital letters and {lowcount} lowercase letters in the string')
count_lower_upper(input('Give string : '),0)