# create a function called create_array() creating 1~3 dimension lists and fetch, obj amount and obj value and print it
# function defining
def create_array(obj_value):
    dimension=[int(input('Enter 1rd list dimension : ')),int(input('Enter 2rd list dimension : ')),nt(input('Enter 3rd list dimension : '))]
    l1 = l2 = l3 = [],[],[]
    for i in range(dimension[2]):
        for i in range(dimension[1]):
            for i in range(dimension[0]):
                l1.append(obj_value)
            l2.append(l1)
            l1=[]
        l3.append(l2)
        l2=[]
    print(f"{l3}")
create_array(input('What is the value per object : '))