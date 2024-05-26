# create a function called create_array() creating 1~3 dimension lists and fetch, obj amount and obj value and print it
# function defining

#input the dimensions and initialization values from user
def create_array(arr_dim, init_value):
    dimension=[0,0,0]
    l1,l2,l3=[],[],[]
    for i in range(1):
        dimension[0]=input('Enter 1rd list dimension : ')
        dimension[1]=input('Enter 2rd list dimension : ')
        dimension[2]=input('Enter 3rd list dimension : ')
    for i in range(dimension[2]):
        for i in range(dimension[1]):
            for i in range(dimension[0]):
                l1.append(obj_value)
            l2.append(l1)
        l3.append(l2)
    print(f"{l3}")

# ask user to input the dimension values (x,y,z)
# get the value for initialization
arr_dim = 0
init_value = 0
create_array(arr_dim,init_value)