import time
x1 = True
def a():
    v1 = int(input('What is 1+1?\n'))
    if v1 != 2:
        x1 == False
    elif v1 == 2:
        x1 == True
    if x1 == False:
        v2 = str(input('Wanna try again?\n'))
        if v2 == 'yes' or 'y':
            print(a())    
    if v1 == 2:
            x1 == True
            print('Yee')
            time.sleep(2.3)
            exit(print('peace!'))
    
a()                