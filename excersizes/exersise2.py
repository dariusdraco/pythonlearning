def compute(integer):
    const=integer
    for i in range(integer):
        integer+=const**i
    print(integer)
compute(int(input('Enter number to compute : ')))
