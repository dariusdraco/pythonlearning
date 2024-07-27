import random as rm
def sanitize_list():
    l1 = [rm.randint(1,30) for _ in range(10)]
    print(f'''
These are the lists whithout duplicates {set(l1)}
And these are the lists with duplicates {l1}
''')
sanitize_list()