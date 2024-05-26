# create a function called create_array() creating 1~3 dimension lists and fetch, obj amount and obj value and print it
# function defining
def create_array(dimension,value,value_num):
    list1d,list2d,list3d=[],[],[]
    if dimension == '1':
        for i in range(value_num):
            list1d.append(value)
    if dimension == '2':
        for i in range(value_num):
                list1d.append(value)
        for i in range(value_num):
            for i in range(value_num):
                list1d.append(value)
            list2d.append(list1d)
    if dimension == '3':
        pass
    else:
        exit(0)
create_array(input('State list dimension 1~3 : '),input('What is value per object : '),input('How many values in a string : '))