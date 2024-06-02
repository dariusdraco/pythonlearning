import random as r 
def create_list():
    l1,l2 = set(r.randint(1,20) for _ in range(10)),set(r.randint(1,20) for _ in range(10))
    print(f'similaty list : {list(l1&l2)}, L1 : {l1} and L2 : {l2}')
create_list()