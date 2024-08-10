import time
last_10_cordinates = list()
x = 0
while True:
    time.sleep(3)
    last_10_cordinates.append(x)
    mod_last_10 = len(last_10_cordinates) % 3
    print(mod_last_10)
    x += 1
    
